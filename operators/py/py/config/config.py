import json
from pathlib import Path
from dataclasses import dataclass
from typing import List


@dataclass
class Chain:
    name: str
    id: int
    wss_endpoint: str
    http_endpoint: str
    vault_address: str


@dataclass
class Config:
    chains: List[Chain]


def load_config(file_path: Path) -> Config:
    with file_path.open() as f:
        data = json.load(f)
        chains = [Chain(**c) for c in data["chains"]]
        return Config(chains=chains)


# Example usage
if __name__ == "__main__":
    config = load_config(Path(__file__).parent / "config.json")
    for chain in config.chains:
        print(f"Chain Name: {chain.name}")
        print(f"Chain ID: {chain.id}")
        print(f"WSS Endpoint: {chain.wss_endpoint}")
        print(f"HTTP Endpoint: {chain.http_endpoint}")
        print(f"Bridge Address: {chain.vault_address}\n")
