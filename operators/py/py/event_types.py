from dataclasses import dataclass
from typing import Any


@dataclass
class BridgeRequest:
    user: str
    token_address: str
    bridge_request_id: int
    amount_in: int
    amount_out: int
    destination_vault: str
    destination_address: str
    transfer_index: int

    def as_struct(self) -> dict[str, Any]:
        return {
            "user": self.user,
            "tokenAddress": self.token_address,
            "bridgeRequestId": self.bridge_request_id,
            "amountIn": self.amount_in,
            "amountOut": self.amount_out,
            "destinationVault": self.destination_vault,
            "destinationAddress": self.destination_address,
            "transferIndex": self.transfer_index
        }


@dataclass
class Attestation:
    attestation: bytes
    bridge_request_id: int
    operator_weight: int


@dataclass
class FundsRelease:
    destination_vault: str
    destination_address: str
    amount_out: int
