// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/src/Test.sol";
import {Vault} from "../src/Vault.sol";
import {TestERC20} from "../src/TestERC20.sol";

import "@openzeppelin/contracts/utils/cryptography/EIP712.sol";
import "../src/Structs.sol";

contract VaultTest is Test, EIP712("Zarathustra", "1") {
    Vault public vault;
    TestERC20 public testERC20;

    Vault public remoteVault;
    TestERC20 public remoteErc20;

    address public deployer;
    address public alice;
    address public bob;
    address public canonicalSigner;
    uint256 public canonicalSignerPkey;
    address public independentSigner;
    uint256 public independentSignerPkey;

    uint256 bridgeFee = 0.005 ether;
    uint256 crankGasCost = 100_000;

    function setUp() public {
        deployer = address(0x4);
        canonicalSigner = address(0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266);
        canonicalSignerPkey = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80;
        //        (canonicalSigner, canonicalSignerPkey) = makeAddrAndKey("canon");
        console.log("Canonical signer: %s", canonicalSigner);
        (independentSigner, independentSignerPkey) = makeAddrAndKey("indep");
        console.log("Independent signer: %s", independentSigner);

        vm.startPrank(deployer);

        vault = new Vault();
        vault.setCanonicalSigner(canonicalSigner);
        testERC20 = new TestERC20();

        vault.setBridgeFee(bridgeFee);

        remoteVault = new Vault();
        remoteErc20 = new TestERC20();

        remoteVault.whitelistSigner(independentSigner);
        remoteVault.setCanonicalSigner(canonicalSigner);

        vm.stopPrank();

        alice = address(0x1);
        bob = address(0x2);

        vm.deal(alice, 1 ether);
        vm.deal(bob, 1 ether);
        vm.deal(address(vault), 1 ether);
        vm.deal(address(remoteVault), 1 ether);

        testERC20.mint(address(remoteVault), 10 ether);
    }

    function test_bridge_e2e() public {
        uint256 amount = 10 * 10 ** 18;
        testERC20.mint(alice, amount);
        remoteErc20.mint(address(remoteVault), amount);

        assertEq(testERC20.balanceOf(alice), amount);
        assertEq(remoteErc20.balanceOf(address(remoteVault)), amount);

        // Alice bridges the tokens
        vm.startPrank(alice);

        Structs.BridgeRequestData memory brd = Structs.BridgeRequestData({
            user: alice,
            tokenAddress: address(testERC20),
            amountIn: amount,
            amountOut: amount,
            destinationVault: address(remoteVault),
            destinationAddress: alice,
            transferIndex: uint256(0),
            canonicalAttestation: abi.encodePacked(uint256(0))
        });

        bytes32 digest = remoteVault.getDigest(brd);

        console.logBytes32(digest);

        (uint8 v1, bytes32 r1, bytes32 s1) = vm.sign(
            canonicalSignerPkey,
            digest
        );

        bytes memory canonicalSig = abi.encodePacked(r1, s1, v1);

        console.logBytes(canonicalSig);

        testERC20.approve(address(vault), amount);
        vault.bridge{value: bridgeFee}({
            tokenAddress: address(testERC20),
            amountIn: amount,
            amountOut: amount,
            destinationVault: address(remoteVault),
            destinationAddress: alice,
            canonicalAttestation: canonicalSig
        });

        vm.stopPrank();

        // Verify Alice's tokens are in the source vault
        assertEq(testERC20.balanceOf(address(vault)), amount);
        assertEq(testERC20.balanceOf(alice), 0);

        vm.startPrank(deployer);
        remoteVault.whitelistSigner(independentSigner);

        (uint8 v2, bytes32 r2, bytes32 s2) = vm.sign(
            independentSignerPkey,
            digest
        );

        // Bob calls the crank with the signatures
        vm.startPrank(bob);

        remoteVault.releaseFunds(
            canonicalSig,
            abi.encodePacked(r2, s2, v2),
            brd
        );

        vm.stopPrank();

        // Verify Alice receives the target tokens
        assertEq(testERC20.balanceOf(alice), amount);

        // Verify Bob receives the crank fee
        assertEq(bob.balance, 1 ether);

        // Verify invalid signatures revert
        bytes32 invalidMessageHash = keccak256(abi.encodePacked(uint256(123)));
        (uint8 v3, bytes32 r3, bytes32 s3) = vm.sign(
            uint256(uint160(canonicalSigner)),
            invalidMessageHash
        );

        vm.expectRevert("Invalid canonical signature");
        remoteVault.releaseFunds(
            abi.encodePacked(r3, s3, v3),
            abi.encodePacked(r2, s2, v2),
            brd
        );

        // Verify non-matching third-party signature reverts
        (uint8 v4, bytes32 r4, bytes32 s4) = vm.sign(
            uint256(uint160(address(0x7))),
            digest
        );

        vm.expectRevert("Invalid signature");
        remoteVault.releaseFunds(
            abi.encodePacked(r1, s1, v1),
            abi.encodePacked(r4, s4, v4),
            brd
        );
    }

    function test_publishAttestation() public {
        vm.startPrank(deployer);
        vault.whitelistSigner(canonicalSigner);

        vm.startPrank(canonicalSigner);

        bytes memory attestation = abi.encodePacked("attestation");
        vault.publishAttestation(attestation, 0);

        vm.stopPrank();
    }
}
