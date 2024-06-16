# Zarathustra (v2)

> run `make update` to update git submodule dependencies

This repository is intended to be the Zarathustra protocol, initially created as a project for ETH Prague 2024, but now being expanded upon for the Eigenlayer hackathon.

![Alt text](image-documentation/zarathustrabanner.png?raw=true "Title")

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

Key contracts:
- `vault.sol`: Manages user interactions and fund management.
- `ZarathustraEigenLayerServiceManager.sol`: Handles operator management and interacts with EigenLayer.

The Zarathustra protocol is primarily driven by two key smart contracts: Vault.sol and ZarathustraEigenLayerServiceManager.sol. Vault.sol serves as the central hub for user interactions and fund management in the cross-chain transfer process. When a user initiates a bridge request, they interact with the Vault contract's bridge function, specifying the token address, amount to transfer, expected output amount, destination vault, and recipient address. The contract securely holds the user's tokens and emits a BridgeRequest event, which is crucial for the subsequent validation process. Vault.sol also manages the release of funds on the destination chain through its releaseFunds function, which requires valid signatures and attestations before executing the transfer.

ZarathustraEigenLayerServiceManager.sol acts as the liaison between the Zarathustra protocol and the EigenLayer ecosystem. This contract is responsible for managing the Actively Validated Service (AVS) operators who play a vital role in validating cross-chain transfers. It handles operator registration, tracks their active status, and ensures they meet the minimum staking requirements. The ServiceManager interacts with EigenLayer's DelegationManager and StrategyManager contracts to verify operator eligibility and manage stakes. When a BridgeRequest event is emitted by the Vault contract, the registered operators, whose status is managed by the ServiceManager, are responsible for validating the request and submitting attestations back to the Vault contract. This interconnected system of contracts ensures a secure, decentralized, and efficient cross-chain transfer mechanism, leveraging EigenLayer's infrastructure for enhanced security and scalability.

To run tests: `make test` cause foundry submodules suck.

### How Zarathustra Works

1. User Interaction:
   - User initiates a transfer through the frontend, specifying amount, currency, and destination chain.
   - Frontend interacts with the `vault.sol` contract.

2. Bridge Request:
   - `vault.sol` receives the bridge request via the `bridge` function.
   - Contract transfers tokens from user to itself.
   - Emits a `BridgeRequest` event and stores request data.

3. AVS Validation:
   - `ZarathustraEigenLayerServiceManager.sol` manages AVS operators.
   - Operators monitor for `BridgeRequest` events.
   - Valid requests are attested to by operators using `publishAttestation`.

4. Fund Release:
   - On the destination chain, `releaseFunds` function is called.
   - Contract verifies signatures and attestations.
   - If valid, transfers tokens to the destination address.

5. EigenLayer Integration:
   - `ZarathustraEigenLayerServiceManager.sol` interacts with EigenLayer contracts for operator staking and management.


