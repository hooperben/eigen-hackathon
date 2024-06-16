import type { NextPage } from "next";
import Head from "next/head";
import { ChangeEvent, useEffect, useState } from "react";
import { ConnectWallet } from "../components/connect-wallet";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "../components/ui/card";

import { Input } from "../components/ui/input";

import { Button } from "../components/ui/button";

import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "../components/ui/dropdown-menu";
import { useAccount, useBalance } from "wagmi";
import Fees from "../components/ui/fees";
import {
  SupportedNetwork,
  supportedNetworks,
  supportedTokens,
} from "../constants/supported-tokens";
import Error from "../components/ui/error";
import { Skeleton } from "../components/ui/skeleton";
import Swaperoo from "../components/ui/swaperoo";
import { parseUnits } from "viem";

const Home: NextPage = () => {
  const { address } = useAccount();

  const [sourceNetwork, setSourceNetwork] =
    useState<SupportedNetwork>("holesky");
  const [destNetwork, setDestNetwork] =
    useState<SupportedNetwork>("op-sepolia");

  // we are just using indexes here - much easier
  const [sourceToken, setSourceToken] = useState<number>(0);
  const [destToken, setDestToken] = useState<number>(1);

  const [bridgeLogicError, setBridgeLogicError] = useState<{
    title: string;
    message: string;
  }>();

  const [amount, setAmount] = useState<number | undefined>(undefined);

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    setAmount(value === "" ? undefined : parseFloat(value));
  };

  const {
    data: sourceTokenBalance,
    refetch,
    isLoading: sourceBalanceLoading,
  } = useBalance({
    address: address,
    token: supportedTokens[sourceToken].address as `0x${string}`,
    chainId: supportedTokens[sourceToken].chainId,
  });

  useEffect(() => {
    refetch();
  }, [refetch, sourceToken]);

  useEffect(() => {
    switch (true) {
      case sourceNetwork === destNetwork:
        setBridgeLogicError({
          title: "Network Mismatch",
          message: "Source and Destination network can't be the same 🥴",
        });
        break;
      case amount &&
        parseUnits(amount!.toString(), supportedTokens[sourceToken].decimals) >
          sourceTokenBalance!.value:
        setBridgeLogicError({
          title: "Insufficient Balance",
          message: "You're trying to send more than you've got",
        });
        break;
      // case (parseUnits(amount) )
      default:
        setBridgeLogicError(undefined);
    }
  }, [amount, destNetwork, sourceNetwork, sourceToken, sourceTokenBalance]);

  const swapSourceAndDest = () => {
    const currentSource = { sourceToken, sourceNetwork };
    const currentDest = { destToken, destNetwork };

    setDestToken(currentSource.sourceToken);
    setDestNetwork(currentSource.sourceNetwork);

    setSourceToken(currentDest.destToken);
    setSourceNetwork(currentDest.destNetwork);
  };

  return (
    <div>
      <Head>
        <title>Zarathustra</title>
        <link href="/favicon.ico" rel="icon" />
      </Head>

      <main className="w-[100%] bg-white">
        <div className="flex w-full justify-between p-4 align-middle">
          <h1>Zarathustra</h1>
          <ConnectWallet />
        </div>

        <div>
          <div className="flex w-full justify-center content-center pt-[200px]">
            <Card className="w-[400px] text-center">
              <CardHeader>
                <CardTitle>Zarathustra</CardTitle>
              </CardHeader>

              <CardContent>
                {/* SOURCE CHAIN AND TOKEN */}
                <div>
                  <div className="pl-4 flex align-left text-xs pb-1">
                    <p>Source Network and Token</p>
                  </div>
                  <div className="px-4 flex justify-between">
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild className="w-40">
                        <Button variant="outline">{sourceNetwork}</Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent className="w-40">
                        {supportedNetworks.map((network) => (
                          <DropdownMenuCheckboxItem
                            key={network}
                            checked={false}
                            onCheckedChange={() => setSourceNetwork(network)}
                          >
                            {network}
                          </DropdownMenuCheckboxItem>
                        ))}
                      </DropdownMenuContent>
                    </DropdownMenu>

                    <div className="flex flex-col">
                      <DropdownMenu>
                        <DropdownMenuTrigger asChild className="w-60">
                          <Button variant="outline">
                            {supportedTokens[sourceToken].name}
                          </Button>
                        </DropdownMenuTrigger>

                        <DropdownMenuContent className="w-60">
                          {supportedTokens.map((token, i) => (
                            <DropdownMenuCheckboxItem
                              key={token.name}
                              checked={i === sourceToken}
                              onCheckedChange={() => setSourceToken(i)}
                            >
                              {token.name}
                            </DropdownMenuCheckboxItem>
                          ))}
                        </DropdownMenuContent>
                      </DropdownMenu>

                      {sourceBalanceLoading && address && (
                        <div className="flex flex-row justify-end pl-4 align-right text-xs pt-1">
                          <Skeleton className="w-[100px] h-[8px] rounded-full" />
                        </div>
                      )}

                      {address &&
                        !sourceBalanceLoading &&
                        sourceTokenBalance &&
                        sourceTokenBalance.formatted && (
                          <div className="flex flex-row justify-end pl-4 align-right text-xs pt-1">
                            <p className="mr-2">Balance:</p>
                            <p>
                              {parseFloat(
                                sourceTokenBalance.formatted
                              ).toLocaleString("en-US", {
                                minimumFractionDigits: 2,
                                maximumFractionDigits: 2,
                              })}
                            </p>
                          </div>
                        )}
                    </div>
                  </div>
                </div>

                <div className="flex justify-center w-full mt-2">
                  <Button onClick={swapSourceAndDest}>
                    <Swaperoo />
                  </Button>
                </div>

                {/* DEST CHAIN AND TOKEN */}
                <div className="pt-5">
                  <div className="pl-4 flex align-left text-xs pb-1">
                    <p>Destination Network and Token</p>
                  </div>
                  <div className="px-4 flex justify-between">
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild className="w-40">
                        <Button variant="outline">{destNetwork}</Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent className="w-40">
                        {supportedNetworks.map((network) => (
                          <DropdownMenuCheckboxItem
                            key={network}
                            checked={destNetwork === network}
                            onCheckedChange={() => setDestNetwork(network)}
                          >
                            {network}
                          </DropdownMenuCheckboxItem>
                        ))}
                      </DropdownMenuContent>
                    </DropdownMenu>

                    <DropdownMenu>
                      <DropdownMenuTrigger asChild className="w-60">
                        <Button variant="outline">
                          {supportedTokens[destToken].name}
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent className="w-60">
                        {supportedTokens.map((token, i) => (
                          <DropdownMenuCheckboxItem
                            key={token.name}
                            checked={i === destToken}
                            onCheckedChange={() => setDestToken(i)}
                          >
                            {token.name}
                          </DropdownMenuCheckboxItem>
                        ))}
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </div>
                </div>

                {/* AMOUNT */}
                <div className="p-4">
                  <div className="flex align-left text-xs pb-1">
                    <p>Amount to Send</p>
                  </div>
                  <Input
                    value={amount !== undefined ? amount : ""}
                    onChange={handleChange}
                    className="bg-white"
                    type="number"
                    placeholder="Amount"
                  />
                </div>

                {bridgeLogicError && (
                  <Error
                    title={bridgeLogicError.title}
                    message={bridgeLogicError.message}
                  />
                )}

                {/* FEES + TRANSFER BREAKDOWN */}
                {/* <Fees /> */}

                {!address && <ConnectWallet />}
              </CardContent>
            </Card>
          </div>
        </div>
      </main>

      <footer></footer>
    </div>
  );
};

export default Home;
