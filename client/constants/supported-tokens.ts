export type SupportedNetwork = "holesky" | "op-sepolia";

interface SupportedToken {
  address: string;
  network: SupportedNetwork;
  name: string;
  chainId: number;
  decimals: number;
}

export const supportedTokens: SupportedToken[] = [
  {
    address: "0x7c127124Fa31D6B321E3a0Fd81F8612Eb1eD7090",
    network: "holesky",
    name: "Test Token (ETH)",
    chainId: 17000,
    decimals: 18,
  },
  {
    address: "0xD30dB776393F8EaEbdF3Ef1E1E609B513eF7c031",
    network: "op-sepolia",
    name: "Test Token (OPS)",
    chainId: 11155420,
    decimals: 18,
  },
];

export const supportedNetworks: SupportedNetwork[] = ["holesky", "op-sepolia"];
