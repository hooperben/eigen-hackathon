"""Generated wrapper for Events Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for Events below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        EventsValidator,
    )
except ImportError:

    class EventsValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Events:
    """Wrapper class for Events Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: EventsValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = EventsValidator(web3_or_provider, contract_address)

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

    def get_avs_attestation_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AVSAttestation event.

        :param tx_hash: hash of transaction emitting AVSAttestation event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Events.abi(),
            )
            .events.AVSAttestation()
            .processReceipt(tx_receipt)
        )

    def get_bridge_request_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for BridgeRequest event.

        :param tx_hash: hash of transaction emitting BridgeRequest event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Events.abi(),
            )
            .events.BridgeRequest()
            .processReceipt(tx_receipt)
        )

    def get_funds_released_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for FundsReleased event.

        :param tx_hash: hash of transaction emitting FundsReleased event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Events.abi(),
            )
            .events.FundsReleased()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"type":"event","name":"AVSAttestation","inputs":[{"name":"attestation","type":"bytes","indexed":true,"internalType":"bytes"},{"name":"bridgeRequestId","type":"uint256","indexed":true,"internalType":"uint256"},{"name":"operatorWeight","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"BridgeRequest","inputs":[{"name":"user","type":"address","indexed":true,"internalType":"address"},{"name":"tokenAddress","type":"address","indexed":true,"internalType":"address"},{"name":"bridgeRequestId","type":"uint256","indexed":true,"internalType":"uint256"},{"name":"amountIn","type":"uint256","indexed":false,"internalType":"uint256"},{"name":"amountOut","type":"uint256","indexed":false,"internalType":"uint256"},{"name":"destinationVault","type":"address","indexed":false,"internalType":"address"},{"name":"destinationAddress","type":"address","indexed":false,"internalType":"address"},{"name":"transferIndex","type":"uint256","indexed":false,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"FundsReleased","inputs":[{"name":"destinationVault","type":"address","indexed":true,"internalType":"address"},{"name":"destinationAddress","type":"address","indexed":true,"internalType":"address"},{"name":"amountOut","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
