import {
  HOLESKY_VAULT_ADDRESS,
  OP_SEPOLIA_VAULT_ADDRESS,
} from "./contract-addresses";

export type SupportedNetwork = "holesky" | "op-sepolia";

interface NetworkDetails {
  name: SupportedNetwork;
  vaultAddress: `0x${string}`;
}

interface SupportedToken {
  address: string;
  network: NetworkDetails;
  name: string;
  chainId: number;
  decimals: number;
  blockExplorer: string;
}

export const supportedTokens: SupportedToken[] = [
  {
    address: "0x7c127124Fa31D6B321E3a0Fd81F8612Eb1eD7090",
    network: { name: "holesky", vaultAddress: HOLESKY_VAULT_ADDRESS },
    name: "Test Token (ETH)",
    chainId: 17000,
    decimals: 18,
    blockExplorer: "https://holesky.etherscan.io/",
  },
  {
    address: "0xD30dB776393F8EaEbdF3Ef1E1E609B513eF7c031",
    network: { name: "op-sepolia", vaultAddress: OP_SEPOLIA_VAULT_ADDRESS },
    name: "Test Token (OPS)",
    chainId: 11155420,
    decimals: 18,
    blockExplorer: "https://sepolia-optimism.etherscan.io/",
  },
];

// this is a bit heinous but CBF
export const supportedTokenWithChainIdIndex: Record<number, SupportedToken> = {
  17000: supportedTokens[0],
  11155420: supportedTokens[1],
};

export const supportedNetworks: SupportedNetwork[] = ["holesky", "op-sepolia"];
