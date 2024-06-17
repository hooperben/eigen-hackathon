import type { NextApiRequest, NextApiResponse } from "next";

import {
  Chain,
  createWalletClient,
  http,
  createPublicClient,
  parseEventLogs,
  verifyTypedData,
  getContract,
  WalletClient,
} from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { holesky, optimismSepolia } from "viem/chains";
import { VaultAbi } from "../../constants/abis/vault";
import { PermissionedBridgeAbi } from "../../constants/abis/permissionedBridge";
import { supportedTokenWithChainIdIndex } from "../../constants/supported-tokens";

const chainIdToChain: Record<number, Chain> = {
  17000: holesky,
  11155420: optimismSepolia,
};

const publishAttestation = async (
  backendWallet: WalletClient,
  chainId: number,
  attestation: string,
  bridgeRequestId: BigInt
) => {
  const contract = getContract({
    address: supportedTokenWithChainIdIndex[chainId].network.vaultAddress,
    abi: PermissionedBridgeAbi,
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
      bridgeRequestId,
      amountIn,
      amountOut,
      destinationVault,
      destinationAddress,
      transferIndex,
      // @ts-ignore -- someone needs to figure this shit out, infuriating
    } = topics[0].args;

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
      chainId: supportedTokenWithChainIdIndex[chainId].chainId,
      verifyingContract:
        supportedTokenWithChainIdIndex[chainId].network.vaultAddress,
    };

    const signed = await account.signTypedData({
      domain,
      types,
      primaryType: "BridgeRequestData",
      message: data,
    });

    const valid = await verifyTypedData({
      address: account.address,
      domain,
      types,
      primaryType: "BridgeRequestData",
      message: data,
      signature: signed,
    });

    console.log("is valid siggie: ", valid);

    // // publish the attestation
    const tx = await publishAttestation(
      backendSigner,
      chainId,
      signed,
      bridgeRequestId
    );

    console.log(tx);

    return res.status(200).json({ txHash: tx, message: "hey" });
  }
}
