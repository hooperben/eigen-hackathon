from pathlib import Path
import json
from eth_account.signers.local import LocalAccount
from web3 import Web3

from py.config.config import Chain
from py.event_types import BridgeRequest

type TransactionHash = str


def load_bridge_abi() -> dict:
    with open(Path(__file__).parent.parent.parent / "abis" / "PermissionedBridge.sol" / "PermissionedBridge.json", "r") as f:
        return json.load(f)["abi"]


class Bridge:
    def __init__(self, chain: Chain):
        self.chain = chain
        self.web3 = Web3(Web3.HTTPProvider(chain.http_endpoint))
        self.bridge_contract = self.web3.eth.contract(address=chain.vault_address, abi=load_bridge_abi())

    def _default_tx_body(self, address: str) -> dict:
        return {
            'from': address,
            'nonce': self.web3.eth.get_transaction_count(address),
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei')
        }

    def _sign_and_send(self, tx, caller: LocalAccount):
        signed_tx = self.web3.eth.account.sign_transaction(tx, caller.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    @property
    def owner(self):
        return self.bridge_contract.functions.owner().call()

    def initialize(self, caller: LocalAccount) -> TransactionHash:
        tx = self.bridge_contract.functions.initialize().build_transaction(
            self._default_tx_body(caller.address)
        )
        return self._sign_and_send(tx, caller)

    def set_bridge_fee(self, caller: LocalAccount):
        tx = self.bridge_contract.functions.setBridgeFee(0).build_transaction(
            self._default_tx_body(caller.address)
        )
        return self._sign_and_send(tx, caller)

    def set_operator_weight(self, operator: str, weight: int, caller: LocalAccount):
        tx = self.bridge_contract.functions.setOperatorWeight(operator, weight).build_transaction(
            self._default_tx_body(caller.address)
        )
        return self._sign_and_send(tx, caller)

    def get_operator_weight(self, operator: str):
        return self.bridge_contract.functions.getOperatorWeight(operator).call()

    def get_digest(self, bridge_request: BridgeRequest):
        return self.bridge_contract.functions.getDigest(bridge_request.as_struct()).call()

    def get_bridge_request(self, bridge_request_id: int):
        return self.bridge_contract.functions.bridgeRequests(bridge_request_id).call()

    def sign_bridge_request(self, bridge_request: BridgeRequest) -> bytes:
        digest = self.get_digest(bridge_request)
        return signer.signHash(digest).signature

    def attest_bridge_request(self, signature: bytes, bridge_request_id: int, caller: LocalAccount) -> str:
        tx = self.bridge_contract.functions.attestBridgeRequest(signature, bridge_request_id).build_transaction(
            self._default_tx_body(caller.address)
        )
        return self._sign_and_send(tx, Account.from_key(self.owner))


if __name__ == "__main__":
    from py.config.config import load_config
    from dotenv import load_dotenv
    import os

    load_dotenv()

    config = load_config(Path(__file__).parent / "config" / "config.json")
    chains = {chain.name: chain for chain in config.chains}
    print(chains.keys())

    b = Bridge(chains["Holesky"])

    from eth_account import Account
    signer = Account.from_key(os.getenv("DEPLOYER_KEY"))

    # print(b.set_operator_weight(signer.address, 10**18, signer))
    # print(b.get_operator_weight(signer.address))
    print("bridge request on ", b.chain.name, b.get_bridge_request(0))
