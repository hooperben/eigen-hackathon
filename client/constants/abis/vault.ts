export const VaultAbi = [
  {
    type: "function",
    name: "AVSReward",
    inputs: [],
    outputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "_releaseFunds",
    inputs: [{ name: "data", type: "bytes", internalType: "bytes" }],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "bridge",
    inputs: [
      {
        name: "tokenAddress",
        type: "address",
        internalType: "address",
      },
      { name: "amountIn", type: "uint256", internalType: "uint256" },
      { name: "amountOut", type: "uint256", internalType: "uint256" },
      {
        name: "destinationVault",
        type: "address",
        internalType: "address",
      },
      {
        name: "destinationAddress",
        type: "address",
        internalType: "address",
      },
    ],
    outputs: [],
    stateMutability: "payable",
  },
  {
    type: "function",
    name: "bridgeFee",
    inputs: [],
    outputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "bridgeRequests",
    inputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    outputs: [
      { name: "user", type: "address", internalType: "address" },
      {
        name: "tokenAddress",
        type: "address",
        internalType: "address",
      },
      { name: "amountIn", type: "uint256", internalType: "uint256" },
      { name: "amountOut", type: "uint256", internalType: "uint256" },
      {
        name: "destinationVault",
        type: "address",
        internalType: "address",
      },
      {
        name: "destinationAddress",
        type: "address",
        internalType: "address",
      },
      {
        name: "transferIndex",
        type: "uint256",
        internalType: "uint256",
      },
    ],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "crankGasCost",
    inputs: [],
    outputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "currentBridgeRequestId",
    inputs: [],
    outputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "eip712Domain",
    inputs: [],
    outputs: [
      { name: "fields", type: "bytes1", internalType: "bytes1" },
      { name: "name", type: "string", internalType: "string" },
      { name: "version", type: "string", internalType: "string" },
      { name: "chainId", type: "uint256", internalType: "uint256" },
      {
        name: "verifyingContract",
        type: "address",
        internalType: "address",
      },
      { name: "salt", type: "bytes32", internalType: "bytes32" },
      {
        name: "extensions",
        type: "uint256[]",
        internalType: "uint256[]",
      },
    ],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "getDigest",
    inputs: [
      {
        name: "data",
        type: "tuple",
        internalType: "struct Structs.BridgeRequestData",
        components: [
          { name: "user", type: "address", internalType: "address" },
          {
            name: "tokenAddress",
            type: "address",
            internalType: "address",
          },
          {
            name: "amountIn",
            type: "uint256",
            internalType: "uint256",
          },
          {
            name: "amountOut",
            type: "uint256",
            internalType: "uint256",
          },
          {
            name: "destinationVault",
            type: "address",
            internalType: "address",
          },
          {
            name: "destinationAddress",
            type: "address",
            internalType: "address",
          },
          {
            name: "transferIndex",
            type: "uint256",
            internalType: "uint256",
          },
        ],
      },
    ],
    outputs: [{ name: "", type: "bytes32", internalType: "bytes32" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "getSigner",
    inputs: [
      {
        name: "data",
        type: "tuple",
        internalType: "struct Structs.BridgeRequestData",
        components: [
          { name: "user", type: "address", internalType: "address" },
          {
            name: "tokenAddress",
            type: "address",
            internalType: "address",
          },
          {
            name: "amountIn",
            type: "uint256",
            internalType: "uint256",
          },
          {
            name: "amountOut",
            type: "uint256",
            internalType: "uint256",
          },
          {
            name: "destinationVault",
            type: "address",
            internalType: "address",
          },
          {
            name: "destinationAddress",
            type: "address",
            internalType: "address",
          },
          {
            name: "transferIndex",
            type: "uint256",
            internalType: "uint256",
          },
        ],
      },
      { name: "signature", type: "bytes", internalType: "bytes" },
    ],
    outputs: [{ name: "", type: "address", internalType: "address" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "initialize",
    inputs: [],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "nextUserTransferIndexes",
    inputs: [{ name: "", type: "address", internalType: "address" }],
    outputs: [{ name: "", type: "uint256", internalType: "uint256" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "owner",
    inputs: [],
    outputs: [{ name: "", type: "address", internalType: "address" }],
    stateMutability: "view",
  },
  {
    type: "function",
    name: "renounceOwnership",
    inputs: [],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "setAVSReward",
    inputs: [{ name: "_AVSReward", type: "uint256", internalType: "uint256" }],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "setBridgeFee",
    inputs: [{ name: "_bridgeFee", type: "uint256", internalType: "uint256" }],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "setCrankGasCost",
    inputs: [
      {
        name: "_crankGasCost",
        type: "uint256",
        internalType: "uint256",
      },
    ],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "function",
    name: "transferOwnership",
    inputs: [{ name: "newOwner", type: "address", internalType: "address" }],
    outputs: [],
    stateMutability: "nonpayable",
  },
  {
    type: "event",
    name: "AVSAttestation",
    inputs: [
      {
        name: "attestation",
        type: "bytes",
        indexed: true,
        internalType: "bytes",
      },
      {
        name: "bridgeRequestId",
        type: "uint256",
        indexed: true,
        internalType: "uint256",
      },
      {
        name: "operatorWeight",
        type: "uint256",
        indexed: true,
        internalType: "uint256",
      },
    ],
    anonymous: false,
  },
  {
    type: "event",
    name: "BridgeRequest",
    inputs: [
      {
        name: "user",
        type: "address",
        indexed: true,
        internalType: "address",
      },
      {
        name: "tokenAddress",
        type: "address",
        indexed: true,
        internalType: "address",
      },
      {
        name: "bridgeRequestId",
        type: "uint256",
        indexed: true,
        internalType: "uint256",
      },
      {
        name: "amountIn",
        type: "uint256",
        indexed: false,
        internalType: "uint256",
      },
      {
        name: "amountOut",
        type: "uint256",
        indexed: false,
        internalType: "uint256",
      },
      {
        name: "destinationVault",
        type: "address",
        indexed: false,
        internalType: "address",
      },
      {
        name: "destinationAddress",
        type: "address",
        indexed: false,
        internalType: "address",
      },
      {
        name: "transferIndex",
        type: "uint256",
        indexed: false,
        internalType: "uint256",
      },
    ],
    anonymous: false,
  },
  {
    type: "event",
    name: "EIP712DomainChanged",
    inputs: [],
    anonymous: false,
  },
  {
    type: "event",
    name: "FundsReleased",
    inputs: [
      {
        name: "destinationVault",
        type: "address",
        indexed: true,
        internalType: "address",
      },
      {
        name: "destinationAddress",
        type: "address",
        indexed: true,
        internalType: "address",
      },
      {
        name: "amountOut",
        type: "uint256",
        indexed: true,
        internalType: "uint256",
      },
    ],
    anonymous: false,
  },
  {
    type: "event",
    name: "Initialized",
    inputs: [
      {
        name: "version",
        type: "uint8",
        indexed: false,
        internalType: "uint8",
      },
    ],
    anonymous: false,
  },
  {
    type: "event",
    name: "OwnershipTransferred",
    inputs: [
      {
        name: "previousOwner",
        type: "address",
        indexed: true,
        internalType: "address",
      },
      {
        name: "newOwner",
        type: "address",
        indexed: true,
        internalType: "address",
      },
    ],
    anonymous: false,
  },
  { type: "error", name: "ECDSAInvalidSignature", inputs: [] },
  {
    type: "error",
    name: "ECDSAInvalidSignatureLength",
    inputs: [{ name: "length", type: "uint256", internalType: "uint256" }],
  },
  {
    type: "error",
    name: "ECDSAInvalidSignatureS",
    inputs: [{ name: "s", type: "bytes32", internalType: "bytes32" }],
  },
  { type: "error", name: "InvalidShortString", inputs: [] },
  { type: "error", name: "ReentrancyGuardReentrantCall", inputs: [] },
  {
    type: "error",
    name: "StringTooLong",
    inputs: [{ name: "str", type: "string", internalType: "string" }],
  },
];
