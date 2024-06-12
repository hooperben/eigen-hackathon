## Zarathustra (v2)

This repository is intended to be the Zarathustra protocol, initially created as a project for ETH Prague 2024, but now being expanded upon for the Eigenlayer hackathon.

### The Zarahustra Protocol

Initially intended to be a cross chain messaging protocol, this example repository is a more specialised implementation that allows for cross chain transfers of ERC20s using an Eigenlayer AVS implementation to accomplish the cross chain messaging.

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

The Vault contract enables seamless cross-chain token transfers using a robust validation mechanism powered by Eigenlayer’s Autonomous Verification Systems (AVS). It employs key libraries from OpenZeppelin for security and efficiency, including IERC20 for token standards, Ownable for access control, ReentrancyGuard to prevent reentrancy attacks, and ECDSA for digital signature operations. Users initiate a bridge request by interacting with the bridge function, transferring tokens to the contract and providing necessary transfer details. The contract emits a BridgeRequest event, logs the request data, and increments internal counters for tracking.

AVS signers, who are pre-approved, validate these bridge requests. They publish attestations via the publishAttestation function, which are then emitted as events and rewarded with ETH. To release funds on the destination chain, the releaseFunds function verifies signatures from both the canonical signer and AVS signers, ensuring the integrity and validity of the transfer. Once verified, the contract transfers the tokens to the specified destination address and pays out a gas cost reward to the caller. This process eliminates intermediaries, reduces costs, and streamlines cross-chain transactions, leveraging smart contracts and AVS for automated, secure, and efficient fund transfers.

To run tests: `make test` cause foundry submodules suck.

### How Zarathustra Works

Starting with the frontend, the user types in their desired amount, currency, and chain. This frontend then interacts directly with the (`vault.sol`) smart contract.

Using the (`vault.sol`) smart contract involves several steps, ensuring secure and efficient cross-chain token transfers. A user starts by initiating a transfer on the source chain through the bridge function. This requires specifying the token address, amount to transfer (`amountIn`), expected amount on the destination chain (`amountOut`), the address of the destination vault, and the recipient’s address on the destination chain. The user must also pay a bridging fee to cover the transaction cost. Upon calling the `bridge` function, the contract transfers the specified tokens from the user to itself using the `bridgeERC20` internal function. This function calls the ERC-20 token’s `transferFrom` method to move the tokens, ensuring the user has approved the transfer beforehand. Once the tokens are successfully transferred, the contract emits a `BridgeRequest` event, logging all necessary details and storing the request data in the `bridgeRequests` mapping. Each request is assigned a unique ID, tracked by `currentBridgeRequestId`.

After the bridge request is made, it waits for validation by an Autonomous Verification System (AVS) signer. AVS signers, who are pre-approved and listed in the `whitelistedSigners` mapping, monitor for new `BridgeRequest` events. Upon detecting a new request, an AVS signer verifies its details and, if valid, publishes an attestation using the `publishAttestation` function. This function emits an `AVSAttestation` event and rewards the AVS signer with a predefined amount of ETH, ensuring the signer’s incentive. The attestation is crucial for the next step, which involves releasing the bridged funds on the destination chain. On the destination chain, another user or automated process calls the `releaseFunds` function with the original request data, the canonical signer's signature, and the AVS signer's attestation signature. The contract first verifies the signatures to ensure authenticity and integrity. Once validated, the contract transfers the specified `amountOut` of tokens to the destination address using the ERC-20 `transfer` function. Additionally, the caller of the `releaseFunds` function is compensated for gas costs based on the current gas price, paid out from the contract’s balance. This completes the cross-chain transfer, providing a seamless and secure mechanism for moving tokens between different blockchains.

