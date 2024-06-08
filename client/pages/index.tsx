import type { NextPage } from "next";
import Head from "next/head";
import { ConnectWallet } from "../components/connect-wallet";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "../components/ui/card";

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Zarathustra</title>
        <link href="/favicon.ico" rel="icon" />
      </Head>

      <main className="w-[100%] bg-white">
        <div className="flex w-full justify-end p-4">
          <ConnectWallet isNavBar />
        </div>

        <div>
          <div className="flex w-full justify-center content-center pt-[200px]">
            <Card className="w-[400px] text-center">
              <CardHeader>
                <CardTitle>Zarathustra</CardTitle>
                {/* <CardDescription>Card Description</CardDescription> */}
              </CardHeader>

              <CardContent>{/* <p>Card Content</p> */}</CardContent>

              <CardFooter>{/* <p>Card Footer</p> */}</CardFooter>
            </Card>
          </div>
        </div>
      </main>

      <footer></footer>
    </div>
  );
};

export default Home;
