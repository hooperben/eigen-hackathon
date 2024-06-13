use ethers::prelude::*;
use eyre::Result;
use std::sync::Arc;

// TODO refactor to vault
abigen!(
    BensContract,
    "../contracts/out/BensContract.sol/BensContract.json",
    event_derives(serde::Deserialize, serde::Serialize)
);

#[tokio::main]

async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = Provider::<Http>::try_from("http://localhost:8545")?;
    let block_number: U64 = provider.get_block_number().await?;
    println!("{block_number}");

    let client = Arc::new(provider);
    let address = "0x5FbDB2315678afecb367f032d93F642f64180aa3" // TODO make dynamic
        .parse::<Address>()
        .unwrap();

    let contract: BensContract<Provider<Http>> = BensContract::new(address, client);

    // need to work out how to make this accept multiple streams for multiple RPCs and Vaults
    listen_all_events(&contract).await?;

    Ok(())
}

async fn listen_all_events(contract: &BensContract<Provider<Http>>) -> Result<()> {
    let events = contract.events().from_block(1);
    let mut stream = events.stream().await?;

    while let Some(Ok(log)) = stream.next().await {
        match log {
            // this should match all events emitted by the vault contract
            BensContractEvents::BensEventFilter(evt) => {
                println!("Event1: {:?}", evt);
            }
            BensContractEvents::BensEvent2Filter(evt) => {
                println!("Event2: {:?}", evt);
            }
        }
    }

    Ok(())
}
