import os

from collections import defaultdict
from eth_account import Account

from py.bridge import Bridge
from py.bridge_monitor import CompositeBridgeMonitor
from py.config.config import Config
from py.event_types import BridgeRequest, Attestation


class AVSOperator:
    def __init__(self, config: Config, signer: Account | None = None):
        self.signer = signer or Account.from_key(os.getenv("AVS_OPERATOR_KEY"))
        self.bridges = {c.name: Bridge(c) for c in config.chains}
        self.bridge_monitor = CompositeBridgeMonitor(*config.chains)

        self.pending_bridge_requests: dict[int, BridgeRequest] = {}
        self.attestations: dict[int, list[Attestation]] = defaultdict(list)

    def sign_and_attest_to_bridge_request(self, chain: str, bridge_request: BridgeRequest) -> str:
        destination_bridge = self.bridges[chain]
        signed_attestation = destination_bridge.sign_bridge_request(bridge_request)
        return destination_bridge.attest_bridge_request(
            signed_attestation, bridge_request.bridge_request_id, self.signer
        )

    async def on_new_bridge_request(self, chain: str, bridge_request: BridgeRequest) -> None:
        print("Received new bridge request: ", bridge_request)
        # Sign and attest the bridge request and send it to the bridge
        self.pending_bridge_requests[bridge_request.bridge_request_id] = bridge_request
        tx_hash = self.sign_and_attest_to_bridge_request(chain, bridge_request)
        print("Attested bridge request: ", bridge_request.bridge_request_id, " with tx hash: ", tx_hash)

    async def on_new_attestation(self, attestation: Attestation):
        # Verify the attestation and check if its exceeded the threshold needed to release the bridge request
        self.attestations[attestation.bridge_request_id].append(attestation)

        if not (for_bridge_request := self.pending_bridge_requests.get(attestation.bridge_request_id)):
            print("Received attestation for unknown bridge request: ", attestation.bridge_request_id)

        attested_stake = sum(a.operator_weight for a in self.attestations[attestation.bridge_request_id])
        if attested_stake >= for_bridge_request.amount_out:
            print("Threshold reached for bridge request: ", attestation.bridge_request_id)
            destination_bridge = self.bridges["OP Sepolioa"]
            signatures = [a.attestation for a in self.attestations[attestation.bridge_request_id]]
            tx_hash = destination_bridge.release_bridge_request(signatures, for_bridge_request, self.signer)
            print("Released bridge request: ", attestation.bridge_request_id, " with tx hash: ", tx_hash)
        else:
            print("Threshold not yet reached for bridge request: ", attestation.bridge_request_id)

    async def run(self):
        async for msg in self.bridge_monitor.monitor():
            # Determine if this is a bridge request or an attestation for a bridge request
            match msg:
                case BridgeRequest() as br:
                    await self.on_new_bridge_request(br)
                case Attestation() as a:
                    await self.on_new_attestation(a)
                case _:
                    print("Unknown message type received from bridge monitor: ", msg)
