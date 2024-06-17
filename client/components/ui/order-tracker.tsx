import { useState } from "react";
import { Progress } from "./progress";
import { useWatchContractEvent } from "wagmi";

import { supportedTokens } from "../../constants/supported-tokens";
import { VaultAbi } from "../../constants/abis/vault";

const OrderTracker = ({
  vaultToWatch,
  address,
}: {
  vaultToWatch: number;
  address: `0x${string}`;
}) => {
  const token = supportedTokens[vaultToWatch];
  const [progressAmount, setProgressAmount] = useState(0);

  const sendBridgeRequestToBackend = async (hash: string, chainId: number) => {
    const response = await fetch("/api/bridge-request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        hash: "",
        chainId: "",
      }),
    });

    if (!response.ok) {
      throw new Error("Error getting history :(");
    }
    const history = await response.json();
  };

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

        sendBridgeRequestToBackend(logs[0].hash, token.chainId);
      }
    },
  });

  // const unwatchBridgeRequest = watchContractEvent(config, {
  //   address: token.network.vaultAddress,
  //   abi: VaultAbi,
  //   chainId: token.chainId as 17000 | 11155420, // TODO fml
  //   eventName: "BridgeRequest",

  //   onLogs(logs) {
  //     console.log(logs.length);
  //     console.log("New logs!", logs);

  //     // @ts-ignore
  //     if (logs[0] && logs[0].args?.user === address) {
  //       console.log("in the if");
  //       setProgressAmount(progressAmount + 33);
  //       unwatchBridgeRequest();
  //     }
  //   },
  // });

  // const unwatchAttestation = watchContractEvent(config, {
  //   address: token.network.vaultAddress,
  //   abi: VaultAbi,
  //   chainId: token.chainId as 17000 | 11155420, // TODO fml
  //   eventName: "AVSAttestation",
  //   onLogs(logs) {
  //     console.log("New logs!", logs);
  //     setProgressAmount(progressAmount + 33);
  //   },
  // });

  return (
    <div className="py-4">
      <Progress value={progressAmount} />
    </div>
  );
};
export default OrderTracker;
