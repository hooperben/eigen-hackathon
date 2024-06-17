# Zarathustra (v2)

> run `make update` to update git submodule dependencies

This repository is intended to be the Zarathustra protocol, initially created as a project for ETH Prague 2024, but now being expanded upon for the Eigenlayer hackathon.

#### [`App`](https://eigen-hackathon.vercel.app/): The Zarathustra Live App
#### [`Docs`](https://docs.zarathustra.cz): The Zarathustra Docs
#### [`Youtube Series`](https://youtube.com/playlist?list=PLQno2E0hjjalvCuOVTP1-WldblsT1-5vR&si=6OyB_HnV_dApC2jv): Zarathustra Video Documentation Series

![Alt text](image-documentation/zarathustrabanner.png?raw=true "Title")

### The Zarahustra Protocol

Initially intended to be a cross chain messaging protocol, this example repository is a more specialised implementation that allows for cross chain transfers of ERC20s using an Eigenlayer AVS implementation. The Zarathustra protocol leverages Eigenlayer's ecosystem to provide secure and efficient cross-chain token transfers.

![Alt text](image-documentation/overview.png?raw=true "Title")

### Components

#### `avs/`

This is the Eigenlayer Active Validator Service. This AVS is written in rust, and more details about what it does and it's structure can be found `avs/README.md`.

to get it running: `cargo build`

#### `client/`

This is the frontend deployed to SITE. This is a NextJS application bootstrapped with:

- wagmi/rainbow kit for wallet connection
- tailwind css for styling

#### `contracts`

This is a foundry project that contains all smart contracts, tests, deployment procedures and scripts required to get all application level (smart contract) parts of the Zarathustra protocol. Within Zarathustra, there are two core smart contracts: `Vault.sol` and `BridgeServiceManager.sol`.

![Alt text](image-documentation/smartcontractdiagram.png?raw=true "Title")

#### The Vault: The Heart of Zarathustra

`Vault.sol` is a Solidity smart contract that serves as the base for our core bridging functionality. It extends multiple modules, including `ECDSAUtils`, `Events`, `ReentrancyGuard`, and `OwnableUpgradeable`, to ensure secure and efficient operations. 

The contract employs several mappings to manage its operations effectively. The `nextUserTransferIndexes` mapping tracks unique transfer indices for each user, ensuring proper sequencing of transfers, while the bridgeRequests mapping stores the history of bridge requests using a globally unique bridge request ID. Additionally, parameters for fees and rewards, such as `bridgeFee`, `AVSReward`, and `crankGasCost`, are stored and can also be adjusted. 

The core functionality of the contract is encapsulated in the bridge function, which handles the initiation of cross-chain transfers. This function ensures that the correct bridge fee is paid, transfers tokens to the contract, emits a `BridgeRequest` event, and stores the request details in the `bridgeRequests` mapping. The `bridgeERC20` function facilitates ERC20 token transfers to the contract, ensuring the seamless handling of token transactions. Furthermore, the contract defines an abstract function `_releaseFunds`, intended to be implemented by inheriting contracts to specify the fund release logic, ensuring flexibility and adaptability in different deployment scenarios.

#### The Bridge Service Manager: Attestations and Operator Management

`BridgeServiceManager.sol` builds upon `Vault.sol` by integrating with the Eigenlayer ecosystem to manage operator attestations and bridge requests. It inherits from `ECDSAServiceManagerBase` and `Vault`, enabling it to interact with Eigenlayer's AVS and stake management features. The contract uses several mappings to track its operations, including `operatorResponses`, which prevents duplicate responses from operators by tracking bridge requests that an operator has responded to, and `bridgeRequestWeights`, which accumulates the total operator weight attested to each bridge request, determining when sufficient attestations have been collected to release funds.

The constructor of `BridgeServiceManager` initializes the contract with addresses for the AVS directory, stake registry, rewards coordinator, and delegation manager, along with parameters for gas cost, AVS reward, and bridge fee. This setup ensures that the contract is well-integrated with the Eigenlayer ecosystem from the outset. Operators interact with the contract primarily through the `publishAttestation` function, which allows them to submit attestations for bridge requests. This function performs several crucial checks, including verifying that the operator has the minimum required weight, ensuring the operator hasn't already responded to the same bridge request, and validating the attestation signature against the bridge request data. Upon passing these checks, the function updates the total weight for the bridge request and rewards the operator for their participation through the `rewardAttestation` function, which calculates and distributes the AVS reward.

To maintain the security and integrity of the system, `BridgeServiceManager` includes a `challengeAttestation` function, which allows any party to challenge potentially fraudulent attestations by providing evidence of a fraudulent signature and bridge request data. If fraud is detected, the contract can penalize the offending operator, thereby providing a strong disincentive for malicious behavior. 

![Alt text](image-documentation/challenge.png?raw=true "Title")

The `releaseFunds` function implements the `_releaseFunds` logic, verifying signatures, summing operator weights, and transferring tokens to the destination address if the total weight is sufficient. This ensures that the release of funds is both secure and efficient. Additionally, the `payoutCrankGasCost` function compensates the user calling the `releaseFunds` function for their gas costs, ensuring that users are incentivized to participate in the protocol.

To run tests: `make test` cause foundry submodules suck.

### How Zarathustra Works

1. First, users interact with our frontend to initiate a bridge request.

2. The frontend calls the Vault smart contract on our home chain, transferring tokens.
After the transfer, the Vault emits an event containing the parameters of the bridge request such as destination chain, token, and amounts.

3. Off-chain, AVS Operators attest to this event. If operators deems the transaction request is valid, the AVS submits an attestation to the bridgeServiceManager smart contract.

4. These attestations are also emitted as public events, and can be challenged by anyone. 
Once sufficient stake has attested that the bridge request is valid, anyone can aggregate the attestations and release the funds on the destination chain.

5. The Vault on the destination chain validates the bridge parameters and attestations, ensuring enough economic value has been staked to cover the released funds, before transferring the user.