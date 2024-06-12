## Zarathustra (v2)

This repository is intended to be the Zarathustra protocol, initially created as a project for ETH Prague 2024, but now being expanded upon for the Eigenlayer hackathon.

### The Zarahustra Protocol

Initially intended to be a cross chain messaging protocol, this example repository is a more specialised implementation that allows for cross chain transfers of ERC20s using an Eigenlayer AVS implementation to accomplish the cross chain messaging.

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
