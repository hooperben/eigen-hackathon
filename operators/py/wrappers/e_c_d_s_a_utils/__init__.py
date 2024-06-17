"""Generated wrapper for ECDSAUtils Solidity contract."""

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
# constructor for ECDSAUtils below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ECDSAUtilsValidator,
    )
except ImportError:

    class ECDSAUtilsValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class StructsBridgeRequestData(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    user: str

    tokenAddress: str

    amountIn: int

    amountOut: int

    destinationVault: str

    destinationAddress: str

    transferIndex: int


class Eip712DomainMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the eip712Domain method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[Union[bytes, str], str, str, int, str, Union[bytes, str], List[int]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (returned[0],returned[1],returned[2],returned[3],returned[4],returned[5],returned[6],)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class GetDigestMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getDigest method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: StructsBridgeRequestData):
        """Validate the inputs to the getDigest method."""
        self.validator.assert_valid(
            method_name='getDigest',
            parameter_name='data',
            argument_value=data,
        )
        return (data)

    def call(self, data: StructsBridgeRequestData, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, data: StructsBridgeRequestData, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(self, data: StructsBridgeRequestData, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, data: StructsBridgeRequestData, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())

class GetSignerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getSigner method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: StructsBridgeRequestData, signature: Union[bytes, str]):
        """Validate the inputs to the getSigner method."""
        self.validator.assert_valid(
            method_name='getSigner',
            parameter_name='data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='getSigner',
            parameter_name='signature',
            argument_value=signature,
        )
        return (data, signature)

    def call(self, data: StructsBridgeRequestData, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data, signature).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, data: StructsBridgeRequestData, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).transact(tx_params.as_dict())

    def build_transaction(self, data: StructsBridgeRequestData, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, data: StructsBridgeRequestData, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ECDSAUtils:
    """Wrapper class for ECDSAUtils Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    eip712_domain: Eip712DomainMethod
    """Constructor-initialized instance of
    :class:`Eip712DomainMethod`.
    """

    get_digest: GetDigestMethod
    """Constructor-initialized instance of
    :class:`GetDigestMethod`.
    """

    get_signer: GetSignerMethod
    """Constructor-initialized instance of
    :class:`GetSignerMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ECDSAUtilsValidator = None,
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
            validator = ECDSAUtilsValidator(web3_or_provider, contract_address)

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
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=ECDSAUtils.abi()).functions

        self.eip712_domain = Eip712DomainMethod(web3_or_provider, contract_address, functions.eip712Domain)

        self.get_digest = GetDigestMethod(web3_or_provider, contract_address, functions.getDigest, validator)

        self.get_signer = GetSignerMethod(web3_or_provider, contract_address, functions.getSigner, validator)

    def get_eip712_domain_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for EIP712DomainChanged event.

        :param tx_hash: hash of transaction emitting EIP712DomainChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ECDSAUtils.abi()).events.EIP712DomainChanged().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"type":"constructor","inputs":[{"name":"name","type":"string","internalType":"string"},{"name":"version","type":"string","internalType":"string"}],"stateMutability":"nonpayable"},{"type":"function","name":"eip712Domain","inputs":[],"outputs":[{"name":"fields","type":"bytes1","internalType":"bytes1"},{"name":"name","type":"string","internalType":"string"},{"name":"version","type":"string","internalType":"string"},{"name":"chainId","type":"uint256","internalType":"uint256"},{"name":"verifyingContract","type":"address","internalType":"address"},{"name":"salt","type":"bytes32","internalType":"bytes32"},{"name":"extensions","type":"uint256[]","internalType":"uint256[]"}],"stateMutability":"view"},{"type":"function","name":"getDigest","inputs":[{"name":"data","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]}],"outputs":[{"name":"","type":"bytes32","internalType":"bytes32"}],"stateMutability":"view"},{"type":"function","name":"getSigner","inputs":[{"name":"data","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]},{"name":"signature","type":"bytes","internalType":"bytes"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"event","name":"EIP712DomainChanged","inputs":[],"anonymous":false},{"type":"error","name":"ECDSAInvalidSignature","inputs":[]},{"type":"error","name":"ECDSAInvalidSignatureLength","inputs":[{"name":"length","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"ECDSAInvalidSignatureS","inputs":[{"name":"s","type":"bytes32","internalType":"bytes32"}]},{"type":"error","name":"InvalidShortString","inputs":[]},{"type":"error","name":"StringTooLong","inputs":[{"name":"str","type":"string","internalType":"string"}]}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
