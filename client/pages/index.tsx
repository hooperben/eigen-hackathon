import type { NextPage } from "next";
import Head from "next/head";
import { useState } from "react";
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
import { useAccount } from "wagmi";

const Home: NextPage = () => {
  const { address } = useAccount();

  const [sourceNetwork, setSourceNetwork] = useState<string>("holesky");
  const [destNetwork, setDestNetwork] = useState<string>("OP Sepolia");

  const [sourceToken, setSourceToken] = useState<string>("ETH");
  const [destToken, setDestToken] = useState<string>("USDC");

  const supportedNetworks = ["holesky", "OP Sepolia"];
  const supportedTokens = ["ETH", "USDC"];

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

                    <DropdownMenu>
                      <DropdownMenuTrigger asChild className="w-60">
                        <Button variant="outline">{sourceToken}</Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent className="w-60">
                        {supportedTokens.map((token) => (
                          <DropdownMenuCheckboxItem
                            key={token}
                            checked={token === sourceToken}
                            onCheckedChange={() => setSourceToken(token)}
                          >
                            {token}
                          </DropdownMenuCheckboxItem>
                        ))}
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </div>
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
                        <Button variant="outline">{destToken}</Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent className="w-60">
                        {supportedTokens.map((token) => (
                          <DropdownMenuCheckboxItem
                            key={token}
                            checked={destToken === token}
                            onCheckedChange={() => setDestToken(token)}
                          >
                            {token}
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
                    className="bg-white"
                    type="number"
                    placeholder="Amount"
                  />
                </div>

                {/* FEES + TRANSFER BREAKDOWN */}
                <div className="p-4">
                  <Card className="p-6 w-full">
                    <h6>Fees</h6>
                  </Card>
                </div>
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
