from pathlib import Path
import json
from web3 import Web3

from py.config.config import Chain


def load_bridge_abi() -> dict:
    with open(Path(__file__).parent.parent.parent / "abis" / "PermissionedBridge.sol" / "PermissionedBridge.json", "r") as f:
        return json.load(f)["abi"]


class Bridge:
    def __init__(self, chain: Chain):
        self.chain = chain
        self.web3 = Web3(Web3.HTTPProvider(chain.http_endpoint))
        self.bridge_contract = self.web3.eth.contract(address=chain.vault_address, abi=load_bridge_abi())


if __name__ == "__main__":
    from py.config.config import load_config
    config = load_config(Path(__file__).parent / "config" / "config.json")
    b = Bridge(config.chains[0])