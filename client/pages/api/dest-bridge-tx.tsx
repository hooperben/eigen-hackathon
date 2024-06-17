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
  getAddress,
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

const chainIdToTokenAddress: Record<number, string> = {
  17000: "0x7c127124Fa31D6B321E3a0Fd81F8612Eb1eD7090",
  11155420: "0xD30dB776393F8EaEbdF3Ef1E1E609B513eF7c031",
};

const sendReleaseFunds = async (
  backendWallet: WalletClient,
  chainId: number,
  attestation: string,
  bridgeRequest: any
) => {
  const contract = getContract({
    address: getAddress(
      supportedTokenWithChainIdIndex[chainId].network.vaultAddress
    ),
    abi: PermissionedBridgeAbi,
    client: { wallet: backendWallet },
  });

  const tx = await contract.write.releaseFunds([[attestation], bridgeRequest]);

  return tx;
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "POST") {
    const { hash, originalHash, chainId, sourceChainId } = req.body;

    console.log(originalHash);
    console.log(chainId);
    console.log(sourceChainId);

    console.log(getAddress(chainIdToTokenAddress[chainId]));
    console.log(supportedTokenWithChainIdIndex[chainId].network.vaultAddress);

    // return res.status(401).json({ message: "ERRRR" });

    const chain = chainIdToChain[parseInt(chainId)];
    const sourceChain = chainIdToChain[parseInt(sourceChainId)];

    if (!chain || !sourceChain)
      return res.status(401).json({ message: "ERRRR" });

    const account = privateKeyToAccount(
      process.env.PRIVATE_KEY! as `0x${string}`
    );

    const sourceChainClient = createPublicClient({
      chain: sourceChain,
      transport: http(),
    });

    const backendSigner = createWalletClient({
      account,
      chain,
      transport: http(),
    });

    const transaction = await sourceChainClient.getTransactionReceipt({
      hash: originalHash,
    });

    const topics = parseEventLogs({
      abi: VaultAbi,
      eventName: "BridgeRequest",
      logs: transaction.logs,
    });

    console.log(topics);

    const {
      user,
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
      tokenAddress: getAddress(chainIdToTokenAddress[chainId]),
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

    const tx = await sendReleaseFunds(backendSigner, chainId, signed, data);

    console.log("post call");

    console.log(tx);

    return res.status(200).json({
      txHash: tx,
      bridgeRequestId: (bridgeRequestId as BigInt).toString(),
    });
  }
}
