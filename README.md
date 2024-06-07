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

to run tests: `make test` cause foundry submodules suck
