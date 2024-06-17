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
  //   eventName: "Attestation",
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
