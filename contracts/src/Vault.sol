// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/EIP712.sol";

import "./Structs.sol";
import "./ZarathustraEigenLayerServiceManager.sol";

contract Vault is Ownable, ReentrancyGuard, EIP712 {
    using ECDSA for bytes32;

    event BridgeRequest(
        address indexed user,
        address indexed tokenAddress,
        uint256 indexed bridgeRequestId,
        uint256 amountIn,
        uint256 amountOut,
        address destinationVault,
        address destinationAddress,
        uint256 transferIndex
    );

    event AVSAttestation(
        bytes indexed attestation,
        uint256 indexed bridgeRequestId
    );

    event FundsReleased(uint256 indexed bridgeRequestId, address destinationAddress, uint256 amount);

    struct Attestation {
    address operator;
    bytes signature;
    }

    mapping(uint256 => Attestation[]) public attestations;
    mapping(uint256 => bool) public validBridgeRequests;
    uint256 public requiredAttestations;

    function setRequiredAttestations(uint256 _requiredAttestations) external onlyOwner {
        requiredAttestations = _requiredAttestations;
    }

    mapping(address => uint256) public nextUserTransferIndexes;
    
    uint256 public currentBridgeRequestId;
    mapping(uint256 => Structs.BridgeRequestData) public bridgeRequests;

    uint256 public bridgeFee;
    uint256 public AVSReward;
    uint256 public crankGasCost;
    address public canonicalSigner;

    ZarathustraEigenLayerServiceManager public eigenLayerServiceManager;

    constructor(address _eigenLayerServiceManager) Ownable(msg.sender) EIP712("Zarathustra", "1") {
        eigenLayerServiceManager = ZarathustraEigenLayerServiceManager(_eigenLayerServiceManager);
        crankGasCost = 0;
        AVSReward = 0;
        bridgeFee = 0;

        canonicalSigner = msg.sender;
        currentBridgeRequestId = 0;
    }

    function setCanonicalSigner(address _canonicalSigner) external onlyOwner {
        canonicalSigner = _canonicalSigner;
    }

    function setBridgeFee(uint256 _bridgeFee) external onlyOwner {
        bridgeFee = _bridgeFee;
    }

    function setAVSReward(uint256 _AVSReward) external onlyOwner {
        AVSReward = _AVSReward;
    }

    function setCrankGasCost(uint256 _crankGasCost) external onlyOwner {
        crankGasCost = _crankGasCost;
    }

    function getDigest(
        Structs.BridgeRequestData memory data
    ) public view returns (bytes32) {
        return
            _hashTypedDataV4(
                keccak256(
                    abi.encode(
                        keccak256(
                            "BridgeRequestData(address user,address tokenAddress,uint256 amountIn,uint256 amountOut,address destinationVault,address destinationAddress,uint256 transferIndex)"
                        ),
                        data.user,
                        data.tokenAddress,
                        data.amountIn,
                        data.amountOut,
                        data.destinationVault,
                        data.destinationAddress,
                        data.transferIndex
                    )
                )
            );
    }

    function getSigner(
        Structs.BridgeRequestData memory data,
        bytes memory signature
    ) public view returns (address) {
        bytes32 digest = getDigest(data);
        return ECDSA.recover(digest, signature);
    }

    function bridgeERC20(address tokenAddress, uint256 amountIn) internal {
        bool success = IERC20(tokenAddress).transferFrom(
            msg.sender,
            address(this),
            amountIn
        );
        require(success, "Transfer failed");
    }

    function bridge(
        address tokenAddress,
        uint256 amountIn,
        uint256 amountOut,
        address destinationVault,
        address destinationAddress
    ) public payable nonReentrant {
        require(msg.value == bridgeFee, "Incorrect bridge fee");

        bridgeERC20(tokenAddress, amountIn);
        uint256 transferIndex = nextUserTransferIndexes[msg.sender];

        emit BridgeRequest(
            msg.sender,
            tokenAddress,
            currentBridgeRequestId,
            amountIn,
            amountOut,
            destinationVault,
            destinationAddress,
            transferIndex
        );

        bridgeRequests[currentBridgeRequestId] = Structs.BridgeRequestData(
            msg.sender,
            tokenAddress,
            amountIn,
            amountOut,
            destinationVault,
            destinationAddress,
            transferIndex
        );

        currentBridgeRequestId++;
        nextUserTransferIndexes[msg.sender]++;

        validateBridgeRequest(
            msg.sender,
            tokenAddress,
            amountIn,
            amountOut,
            destinationVault,
            destinationAddress,
            transferIndex,
            currentBridgeRequestId
        );
    }

        function validateBridgeRequest(
            address user,
            address tokenAddress,
            uint256 amountIn,
            uint256 amountOut,
            address destinationVault,
            address destinationAddress,
            uint256 transferIndex,
            uint256 bridgeRequestId
        ) internal view returns (bool isValid) {

        // Check if the bridge request exists and matches the provided data

        Structs.BridgeRequestData memory request = bridgeRequests[bridgeRequestId];
        require(request.user == user, "User mismatch");
        require(request.tokenAddress == tokenAddress, "Token mismatch");
        require(request.amountIn == amountIn, "Amount in mismatch");
        require(request.amountOut == amountOut, "Amount out mismatch");
        require(request.destinationVault == destinationVault, "Destination vault mismatch");
        require(request.destinationAddress == destinationAddress, "Destination address mismatch");
        require(request.transferIndex == transferIndex, "Transfer index mismatch");

        // Some more additional checks

        require(amountIn > 0 && amountOut > 0, "Invalid amounts");
        require(user != address(0) && destinationAddress != address(0), "Invalid addresses");
        
        // Check if the user has sufficient balance

        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(user) >= amountIn, "Insufficient balance");

        // Perhaps we check if the destination vault is whitelisted?
        // require(isWhitelistedVault(destinationVault), "Invalid destination vault");

        return true;
    }

    function publishAttestation(
        uint256 bridgeRequestId,
        bytes memory signature
    ) public nonReentrant {
        require(eigenLayerServiceManager.isActiveOperator(msg.sender), "Invalid AVS operator");

        Structs.BridgeRequestData memory request = bridgeRequests[bridgeRequestId];
        
        // Verify the operator's signature

        bytes32 messageHash = keccak256(abi.encodePacked(
            bridgeRequestId,
            request.user,
            request.tokenAddress,
            request.amountIn,
            request.amountOut,
            request.destinationVault,
            request.destinationAddress,
            request.transferIndex
        ));
        require(ECDSA.recover(messageHash, signature) == msg.sender, "Invalid signature");

        // Store the attestation

        attestations[bridgeRequestId].push(Attestation(msg.sender, signature));

        emit AVSAttestation(signature, bridgeRequestId);

        // If we have enough attestations, mark the bridge request as valid
        if (attestations[bridgeRequestId].length >= requiredAttestations) {
            validBridgeRequests[bridgeRequestId] = true;
        }

        // Pay the operator

        uint256 payout = AVSReward;
        if (address(this).balance < payout) {
            payout = address(this).balance;
        }

        (bool sent, ) = msg.sender.call{value: payout}("");
        require(sent, "Failed to send AVS reward");
    }

    function releaseFunds(
    bytes memory canonicalSignature,
    Structs.BridgeRequestData memory data
    ) public nonReentrant {

        uint256 bridgeRequestId = getBridgeRequestId(data);
        require(validBridgeRequests[bridgeRequestId], "Bridge request not validated by AVS");

        // Verify canonical signer's signature

        require(
            getSigner(data, canonicalSignature) == canonicalSigner,
            "Invalid canonical signature"
        );

        require(
            data.destinationVault == address(this),
            "Invalid destination vault"
        );

        // Verify that the provided data matches the stored bridge request

        Structs.BridgeRequestData memory storedData = bridgeRequests[bridgeRequestId];
        require(
            keccak256(abi.encode(data)) == keccak256(abi.encode(storedData)),
            "Provided data does not match stored bridge request"
        );

        IERC20(data.tokenAddress).approve(address(this), data.amountOut);
        IERC20(data.tokenAddress).transfer(
            data.destinationAddress,
            data.amountOut
        );

        uint256 payout = crankGasCost * tx.gasprice;
        if (address(this).balance < payout) {
            payout = address(this).balance;
        }

        if (payout > 0) {
            (bool sent, ) = msg.sender.call{value: payout}("");
            require(sent, "Failed to send crank fee");
        }

        // Mark the bridge request as processed to prevent double-spending

        delete validBridgeRequests[bridgeRequestId];
        delete bridgeRequests[bridgeRequestId];

        emit FundsReleased(bridgeRequestId, data.destinationAddress, data.amountOut);
    }

    // Helper function to get the bridge request ID

    function getBridgeRequestId(Structs.BridgeRequestData memory data) public pure returns (uint256) {
        return uint256(keccak256(abi.encode(
            data.user,
            data.tokenAddress,
            data.amountIn,
            data.amountOut,
            data.destinationVault,
            data.destinationAddress,
            data.transferIndex
        )));
    }

    receive() external payable {}
}