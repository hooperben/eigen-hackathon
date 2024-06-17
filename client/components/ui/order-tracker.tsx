import { Dispatch, SetStateAction, useEffect, useState } from "react";
import { useTransactionReceipt, useWatchContractEvent } from "wagmi";
import { PermissionedBridgeAbi } from "../../constants/abis/permissionedBridge";
import { VaultAbi } from "../../constants/abis/vault";
import {
  supportedTokenWithChainIdIndex,
  supportedTokens,
} from "../../constants/supported-tokens";
import { Button } from "./button";
import { Progress } from "./progress";
import Spinner from "./spinner";

const OrderTracker = ({
  vaultToWatch,
  address,
  orderComplete,
  setOrderComplete,
  destChainId,
}: {
  vaultToWatch: number;
  address: `0x${string}`;
  orderComplete: boolean;
  setOrderComplete: Dispatch<SetStateAction<boolean>>;
  destChainId: number;
}) => {
  const token = supportedTokens[vaultToWatch];
  const [progressAmount, setProgressAmount] = useState(0);

  const [bridgeRequestId, setBridgeRequestId] = useState<number>();

  const [originalBridgeTxHash, setOriginalBridgeTxHash] = useState<string>();
  const [destinationHash, setDestinationHash] = useState<string>();

  const sendBridgeRequestToBackend = async (hash: string, chainId: number) => {
    setOriginalBridgeTxHash(hash);
    const response = await fetch("/api/bridge-request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        hash,
        chainId,
      }),
    });

    if (!response.ok) {
      throw new Error("Error calling AVS :(");
    }
    const backendHash = await response.json();

    setBridgeRequestId(backendHash.bridgeRequestId);
  };

  const sendRequestToMintOnDest = async (hash: string, chainId: number) => {
    const response = await fetch("/api/dest-bridge-tx", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        originalHash: originalBridgeTxHash,
        hash,
        chainId: chainId,
        sourceChainId: token.chainId,
      }),
    });

    if (!response.ok) {
      throw new Error("Error Minting on Dest :(");
    }
    const backendHash = await response.json();

    setDestinationHash(backendHash.txHash);
  };

  const { isSuccess } = useTransactionReceipt({
    hash: destinationHash as `0x${string}` | undefined,
    chainId: supportedTokenWithChainIdIndex[destChainId].chainId,
  });

  useEffect(() => {
    if (isSuccess) {
      setProgressAmount(100);
      setOrderComplete(true);
    }
  }, [isSuccess]);

  // listen for BridgeRequest events
  useWatchContractEvent({
    address: token.network.vaultAddress,
    abi: VaultAbi,
    chainId: token.chainId as 17000 | 11155420, // TODO fml
    eventName: "BridgeRequest",

    onLogs(logs: any) {
      console.log(logs.length);
      console.log("New logs!", logs);

      // @ts-ignore
      if (logs[0] && logs[0].args?.user === address) {
        console.log("got the users bridge request");
        setProgressAmount(progressAmount + 33);

        sendBridgeRequestToBackend(logs[0].transactionHash, token.chainId);
      }
    },
  });

  useWatchContractEvent({
    address: token.network.vaultAddress,
    abi: PermissionedBridgeAbi,
    chainId: token.chainId as 17000 | 11155420, // TODO fml
    eventName: "AVSAttestation",

    onLogs(logs: any) {
      console.log(logs.length);
      console.log("New logs!", logs);

      // @ts-ignore
      if (
        bridgeRequestId &&
        logs[0] &&
        logs[0].args?.bridgeRequestId === BigInt(bridgeRequestId?.toString())
      ) {
        console.log("in the AVSAttestation if");
        setProgressAmount(progressAmount + 33);

        sendRequestToMintOnDest(logs[0].transactionHash, destChainId);
      }
    },
  });

  return (
    <div className="py-4">
      <Progress value={progressAmount} />

      {!orderComplete && <Spinner />}

      {progressAmount === 0 && (
        <p className="text-xs">Submitting your bridge request.</p>
      )}

      {progressAmount === 33 && (
        <p className="text-xs">
          Your bridge request has been picked up by the AVS..
        </p>
      )}

      {progressAmount === 66 && (
        <p className="text-xs">
          The AVS has attested to your transaction and it is being relayed to
          the destination chain
        </p>
      )}

      {progressAmount === 100 && (
        <>
          <Button
            onClick={() =>
              window.open(
                `${supportedTokenWithChainIdIndex[destChainId].blockExplorer}/tx/${destinationHash}`,
                "_blank",
                "noopener,noreferrer"
              )
            }
          >
            View on Explorer
          </Button>
          <p className="text-xs">
            Your tokens have arrived on the destination chain!
          </p>
        </>
      )}
    </div>
  );
};
export default OrderTracker;
