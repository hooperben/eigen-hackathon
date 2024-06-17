import type { NextApiRequest, NextApiResponse } from "next";

import {
  Chain,
  createWalletClient,
  http,
  createPublicClient,
  parseEventLogs,
  PublicClient,
  verifyTypedData,
  getContract,
  WalletClient,
} from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { holesky, optimismSepolia } from "viem/chains";
import { VaultAbi } from "../../constants/abis/vault";
import { supportedTokenWithChainIdIndex } from "../../constants/supported-tokens";

const chainIdToChain: Record<number, Chain> = {
  17000: holesky,
  11155420: optimismSepolia,
};

// const getDigest = async (
//   publicClient: PublicClient,
//   chainId: number,
//   args: any
// ) =>
//   await publicClient.readContract({
//     address: supportedTokenWithChainIdIndex[chainId].network.vaultAddress,
//     abi: VaultAbi,
//     functionName: "getDigest",
//     args,
//   });

const publishAttestation = async (
  backendWallet: WalletClient,
  chainId: number,
  attestation: string,
  bridgeRequestId: BigInt
) => {
  const contract = getContract({
    address: supportedTokenWithChainIdIndex[chainId].network.vaultAddress,
    abi: VaultAbi,
    client: { wallet: backendWallet },
  });

  const tx = await contract.write.publishAttestation([
    attestation,
    bridgeRequestId,
  ]);
  return tx;
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    const { hash, chainId } = req.body;

    console.log(hash);

    const chain = chainIdToChain[parseInt(chainId)];

    if (!chain) return res.status(401).json({ message: "ERRRR" });

    const account = privateKeyToAccount(
      process.env.PRIVATE_KEY! as `0x${string}`
    );

    const publicClient = createPublicClient({
      chain,
      transport: http(),
    });

    const backendSigner = createWalletClient({
      account,
      chain,
      transport: http(),
    });

    const transaction = await publicClient.getTransactionReceipt({ hash });

    const topics = parseEventLogs({
      abi: VaultAbi,
      eventName: "BridgeRequest",
      logs: transaction.logs,
    });

    const {
      user,
      tokenAddress,
      amountIn,
      amountOut,
      destinationVault,
      destinationAddress,
      transferIndex,
      // @ts-ignore -- someone needs to figure this shit out, infuriating
    } = topics[0].args;

    // const args = [
    //   {
    //     user,
    //     tokenAddress,
    //     amountIn,
    //     amountOut,
    //     destinationVault,
    //     destinationAddress,
    //     transferIndex,
    //   },
    // ];

    // const digest = await getDigest(publicClient, chainId, args);

    const data: {
      user: string;
      tokenAddress: string;
      amountIn: BigInt;
      amountOut: BigInt;
      destinationVault: string;
      destinationAddress: string;
      transferIndex: BigInt;
    } = {
      user,
      tokenAddress,
      amountIn,
      amountOut,
      destinationVault,
      destinationAddress,
      transferIndex,
    };

    const types = {
      BridgeRequestData: [
        { name: "user", type: "address" },
        { name: "tokenAddress", type: "address" },
        { name: "amountIn", type: "uint256" },
        { name: "amountOut", type: "uint256" },
        { name: "destinationVault", type: "address" },
        { name: "destinationAddress", type: "address" },
        { name: "transferIndex", type: "uint256" },
      ],
    };

    const domain = {
      name: "Zarathustra",
      version: "3",
    };

    const signed = await backendSigner.signTypedData({
      account,
      domain,
      types,
      primaryType: "BridgeRequestData",
      message: data,
    });

    console.log(signed);

    const valid = await verifyTypedData({
      address: account.address,
      domain,
      types,
      primaryType: "BridgeRequestData",
      message: data,
      signature: signed,
    });

    console.log("is valid siggie: ", valid);

    return res.status(200).json({ message: "hey" });
  }
}
