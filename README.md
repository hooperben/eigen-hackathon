# Zarathustra (v2)

> run `make update` to update git submodule dependencies

This repository is intended to be the Zarathustra protocol, initially created as a project for ETH Prague 2024, but now being expanded upon for the Eigenlayer hackathon.

![Alt text](image-documentation/zarathustrabanner.png?raw=true "Title")

### The Zarahustra Protocol

Initially intended to be a cross chain messaging protocol, this example repository is a more specialised implementation that allows for cross chain transfers of ERC20s using an Eigenlayer AVS implementation. The Zarathustra protocol leverages Eigenlayer's infrastructure to provide secure and efficient cross-chain token transfers. At its core, the protocol utilizes a smart contract called VaultAVS, which combines the functionality of a vault and an AVS manager.

### [`VaultAVS.sol`](https://docs.zarathustra.cz): The Zarathustra Docs
### [`VaultAVS.sol`](https://youtube.com): Youtube Video Tutorial Series

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

This is a foundry project that contains all smart contracts, tests, deployment procedures and scripts required to get all application level (smart contract) parts of the Zarathustra protocol.

#### The Vault: The Heart of Zarathustra

`VaultAVS.sol` is a Solidity smart contract that integrates vault functionality with AVS management. It inherits from `ECDSAServiceManagerBase`, allowing it to interact seamlessly with Eigenlayer's ecosystem. The contract uses several mappings to efficiently track bridge requests, operator responses, and weights.

`nextUserTransferIndexes`: This mapping keeps track of unique transfer indices for each user, ensuring proper sequencing of transfers.

`operatorResponses`: This prevents duplicate responses from operators, maintaining the integrity of the validation process.

`bridgeRequestWeights`: This accumulates the total weight of operators attesting to each request, crucial for determining when a transfer can be executed.

The contract's `bridge` function serves as the entry point for users initiating cross-chain transfers. It accepts token transfers and emits a `BridgeRequest` event, storing the request details in the `bridgeRequests` mapping. This function ensures that the correct bridge fee is paid and that the token transfer to the contract is successful.

Operators interact with the contract through the `publishAttestation` function. This function performs several crucial checks. It verifies that the operator has the minimum required weight, ensures the operator hasn't already responded to the same bridge request, and validates the attestation signature against the bridge request data. Upon passing these checks, the function updates the total weight for the bridge request and rewards the operator for their participation.

To maintain the security and integrity of the system, `VaultAVS.sol` includes a `challengeAttestation` function. This allows any party to challenge a potentially fraudulent attestation by providing evidence of the fraudulent signature and bridge request data. If fraud is detected, the contract can slash the offending operator, providing a strong disincentive for malicious behavior.

![Alt text](image-documentation/challenge.png?raw=true "Title")

The contract also includes several helper functions for managing operator weights and minimum requirements, as well as owner-only functions for adjusting fees and rewards. These functions allow for fine-tuning of the protocol's economic parameters as needed. 

The contract's integration with Eigenlayer's stake registry and rewards coordinator allows it to leverage the security and economic incentives of the broader Eigenlayer ecosystem.

To run tests: `make test` cause foundry submodules suck.

### How Zarathustra Works

1. User Interaction: Users initiate transfers through the frontend, specifying the amount, currency, and destination chain. The frontend interacts with the `VaultAVS.sol` contract to process this request.

2. Bridge Request: The `VaultAVS.sol` contract receives the bridge request via the `bridge` function. It transfers tokens from the user to itself and emits a `BridgeRequest` event, storing the request data for future reference.

3. AVS Validation: The `VaultAVS.sol` contract, which incorporates AVS management functionality, oversees the validation process. Registered operators monitor for `BridgeRequest` events and attest to valid requests using the `publishAttestation` function As attestations are emitted as public events, they can be challenged by anyone via the `challengeAttestation` function.

4. Fund Release: Once sufficient stake has attested that the bridge request is valid, anyone can aggregate the attestations and release the funds on the destination chain by calling the `releaseFunds` function. This function verifies signatures and attestations before transferring tokens to the destination address.

5. The Vault on the destination chain validates the bridge parameters and attestations, ensuring enough economic value has been staked to cover the released funds, before completing the process by transferring the user.