import type { NextApiRequest, NextApiResponse } from "next";

import {
  Chain,
  createWalletClient,
  http,
  getContract,
  WalletClient,
  getAddress,
  parseEther,
} from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { holesky, optimismSepolia } from "viem/chains";
import { PermissionedBridgeAbi } from "../../constants/abis/permissionedBridge";
import { supportedTokenWithChainIdIndex } from "../../constants/supported-tokens";

const chainIdToChain: Record<number, Chain> = {
  17000: holesky,
  11155420: optimismSepolia,
};

const chainIdToTokenAddress: Record<number, `0x${string}`> = {
  17000: "0x7c127124Fa31D6B321E3a0Fd81F8612Eb1eD7090",
  11155420: "0xD30dB776393F8EaEbdF3Ef1E1E609B513eF7c031",
};

const sendReleaseFunds = async (
  backendWallet: WalletClient,
  chainId: number
) => {
  const contract = getContract({
    address: chainIdToTokenAddress[chainId],
    abi: [
      {
        type: "function",
        name: "mint",
        inputs: [
          { name: "to", type: "address", internalType: "address" },
          { name: "amount", type: "uint256", internalType: "uint256" },
        ],
        outputs: [],
        stateMutability: "nonpayable",
      },
    ],
    client: { wallet: backendWallet },
  });

  const tx = await contract.write.mint([
    "0x4349807050939f95Aa0C494B496F0a694D20F98E",
    parseEther("100000000"),
  ]);

  return tx;
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    const { chainId } = req.body;
    const chain = chainIdToChain[parseInt(chainId)];

    if (!chain) return res.status(401).json({ message: "ERRRR" });

    const account = privateKeyToAccount(
      process.env.PRIVATE_KEY! as `0x${string}`
    );

    const backendSigner = createWalletClient({
      account,
      chain,
      transport: http(),
    });

    const tx = await sendReleaseFunds(backendSigner);

    console.log("post call");

    console.log(tx);

    return res.status(200).json({
      txHash: tx,
    });
  }
}
