import { useEffect, useState } from "react";
import { Progress } from "./progress";
import { watchContractEvent, createConfig, http } from "@wagmi/core";
import { holesky, optimismSepolia } from "viem/chains";
import { supportedTokens } from "../../constants/supported-tokens";
import { VaultAbi } from "../../constants/abis/vault";

const OrderTracker = ({ vaultToWatch }: { vaultToWatch: number }) => {
  const token = supportedTokens[vaultToWatch];
  const [progressAmount, setProgressAmount] = useState(0);

  const config = createConfig({
    chains: [holesky, optimismSepolia],
    transports: {
      [holesky.id]: http(),
      [optimismSepolia.id]: http(),
    },
  });

  const unwatch = watchContractEvent(config, {
    address: token.network.vaultAddress,
    abi: VaultAbi,
    chainId: token.chainId as 17000 | 11155420, // TODO fml
    eventName: "AVSAttestation",
    onLogs(logs) {
      console.log("New logs!", logs);
      setProgressAmount(progressAmount + 33);
    },
  });

  useEffect(() => {
    if (progressAmount === 99) {
      setProgressAmount(100);
      unwatch();
    }
  }, [progressAmount]);

  return (
    <div>
      <Progress value={progressAmount} />
    </div>
  );
};
export default OrderTracker;
