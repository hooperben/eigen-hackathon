"""Generated wrapper for BridgeServiceManager Solidity contract."""

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
# constructor for BridgeServiceManager below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        BridgeServiceManagerValidator,
    )
except ImportError:

    class BridgeServiceManagerValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IRewardsCoordinatorStrategyAndMultiplier(TypedDict):
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

    strategy: str

    multiplier: int


class IRewardsCoordinatorRewardsSubmission(TypedDict):
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

    strategiesAndMultipliers: List[IRewardsCoordinatorStrategyAndMultiplier]

    token: str

    amount: int

    startTimestamp: int

    duration: int


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


class ISignatureUtilsSignatureWithSaltAndExpiry(TypedDict):
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

    signature: Union[bytes, str]

    salt: Union[bytes, str]

    expiry: int


class AvsRewardMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the AVSReward method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class ReleaseFunds_Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the _releaseFunds method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: Union[bytes, str]):
        """Validate the inputs to the _releaseFunds method."""
        self.validator.assert_valid(
            method_name="_releaseFunds",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(data).call(tx_params.as_dict())

    def send_transaction(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class AvsDirectoryMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the avsDirectory method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class BridgeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the bridge method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        token_address: str,
        amount_in: int,
        amount_out: int,
        destination_vault: str,
        destination_address: str,
    ):
        """Validate the inputs to the bridge method."""
        self.validator.assert_valid(
            method_name="bridge",
            parameter_name="tokenAddress",
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        self.validator.assert_valid(
            method_name="bridge",
            parameter_name="amountIn",
            argument_value=amount_in,
        )
        # safeguard against fractional inputs
        amount_in = int(amount_in)
        self.validator.assert_valid(
            method_name="bridge",
            parameter_name="amountOut",
            argument_value=amount_out,
        )
        # safeguard against fractional inputs
        amount_out = int(amount_out)
        self.validator.assert_valid(
            method_name="bridge",
            parameter_name="destinationVault",
            argument_value=destination_vault,
        )
        destination_vault = self.validate_and_checksum_address(
            destination_vault
        )
        self.validator.assert_valid(
            method_name="bridge",
            parameter_name="destinationAddress",
            argument_value=destination_address,
        )
        destination_address = self.validate_and_checksum_address(
            destination_address
        )
        return (
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        )

    def call(
        self,
        token_address: str,
        amount_in: int,
        amount_out: int,
        destination_vault: str,
        destination_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ) = self.validate_and_normalize_inputs(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_address: str,
        amount_in: int,
        amount_out: int,
        destination_vault: str,
        destination_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ) = self.validate_and_normalize_inputs(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_address: str,
        amount_in: int,
        amount_out: int,
        destination_vault: str,
        destination_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ) = self.validate_and_normalize_inputs(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_address: str,
        amount_in: int,
        amount_out: int,
        destination_vault: str,
        destination_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ) = self.validate_and_normalize_inputs(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address,
            amount_in,
            amount_out,
            destination_vault,
            destination_address,
        ).estimateGas(tx_params.as_dict())


class BridgeFeeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the bridgeFee method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class BridgeRequestWeightsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the bridgeRequestWeights method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the bridgeRequestWeights method."""
        self.validator.assert_valid(
            method_name="bridgeRequestWeights",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class BridgeRequestsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the bridgeRequests method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the bridgeRequests method."""
        self.validator.assert_valid(
            method_name="bridgeRequests",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, str, int, int, str, str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
            returned[4],
            returned[5],
            returned[6],
        )

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class ChallengeAttestationMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the challengeAttestation method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        fraudulent_signature: Union[bytes, str],
        fraudulent_bridge_request: StructsBridgeRequestData,
    ):
        """Validate the inputs to the challengeAttestation method."""
        self.validator.assert_valid(
            method_name="challengeAttestation",
            parameter_name="fraudulentSignature",
            argument_value=fraudulent_signature,
        )
        self.validator.assert_valid(
            method_name="challengeAttestation",
            parameter_name="fraudulentBridgeRequest",
            argument_value=fraudulent_bridge_request,
        )
        return (fraudulent_signature, fraudulent_bridge_request)

    def call(
        self,
        fraudulent_signature: Union[bytes, str],
        fraudulent_bridge_request: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (fraudulent_signature, fraudulent_bridge_request) = (
            self.validate_and_normalize_inputs(
                fraudulent_signature, fraudulent_bridge_request
            )
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            fraudulent_signature, fraudulent_bridge_request
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        fraudulent_signature: Union[bytes, str],
        fraudulent_bridge_request: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (fraudulent_signature, fraudulent_bridge_request) = (
            self.validate_and_normalize_inputs(
                fraudulent_signature, fraudulent_bridge_request
            )
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            fraudulent_signature, fraudulent_bridge_request
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        fraudulent_signature: Union[bytes, str],
        fraudulent_bridge_request: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (fraudulent_signature, fraudulent_bridge_request) = (
            self.validate_and_normalize_inputs(
                fraudulent_signature, fraudulent_bridge_request
            )
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            fraudulent_signature, fraudulent_bridge_request
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        fraudulent_signature: Union[bytes, str],
        fraudulent_bridge_request: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (fraudulent_signature, fraudulent_bridge_request) = (
            self.validate_and_normalize_inputs(
                fraudulent_signature, fraudulent_bridge_request
            )
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            fraudulent_signature, fraudulent_bridge_request
        ).estimateGas(tx_params.as_dict())


class CrankGasCostMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the crankGasCost method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class CreateAvsRewardsSubmissionMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the createAVSRewardsSubmission method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, rewards_submissions: List[IRewardsCoordinatorRewardsSubmission]
    ):
        """Validate the inputs to the createAVSRewardsSubmission method."""
        self.validator.assert_valid(
            method_name="createAVSRewardsSubmission",
            parameter_name="rewardsSubmissions",
            argument_value=rewards_submissions,
        )
        return rewards_submissions

    def call(
        self,
        rewards_submissions: List[IRewardsCoordinatorRewardsSubmission],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (rewards_submissions) = self.validate_and_normalize_inputs(
            rewards_submissions
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(rewards_submissions).call(tx_params.as_dict())

    def send_transaction(
        self,
        rewards_submissions: List[IRewardsCoordinatorRewardsSubmission],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (rewards_submissions) = self.validate_and_normalize_inputs(
            rewards_submissions
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_submissions).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        rewards_submissions: List[IRewardsCoordinatorRewardsSubmission],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (rewards_submissions) = self.validate_and_normalize_inputs(
            rewards_submissions
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_submissions).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        rewards_submissions: List[IRewardsCoordinatorRewardsSubmission],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (rewards_submissions) = self.validate_and_normalize_inputs(
            rewards_submissions
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_submissions).estimateGas(
            tx_params.as_dict()
        )


class CurrentBridgeRequestIdMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the currentBridgeRequestId method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class DeregisterOperatorFromAvsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the deregisterOperatorFromAVS method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the deregisterOperatorFromAVS method."""
        self.validator.assert_valid(
            method_name="deregisterOperatorFromAVS",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator).call(tx_params.as_dict())

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(
            tx_params.as_dict()
        )


class Eip712DomainMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the eip712Domain method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> Tuple[
        Union[bytes, str], str, str, int, str, Union[bytes, str], List[int]
    ]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
            returned[4],
            returned[5],
            returned[6],
        )

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class GetDigestMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getDigest method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: StructsBridgeRequestData):
        """Validate the inputs to the getDigest method."""
        self.validator.assert_valid(
            method_name="getDigest",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self,
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class GetOperatorRestakedStrategiesMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getOperatorRestakedStrategies method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the getOperatorRestakedStrategies method."""
        self.validator.assert_valid(
            method_name="getOperatorRestakedStrategies",
            parameter_name="_operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(operator).call(tx_params.as_dict())
        return [str(element) for element in returned]

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(
            tx_params.as_dict()
        )


class GetOperatorWeightMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getOperatorWeight method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the getOperatorWeight method."""
        self.validator.assert_valid(
            method_name="getOperatorWeight",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(self, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(operator).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(
            tx_params.as_dict()
        )


class GetRestakeableStrategiesMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getRestakeableStrategies method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [str(element) for element in returned]

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class GetSignerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getSigner method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, data: StructsBridgeRequestData, signature: Union[bytes, str]
    ):
        """Validate the inputs to the getSigner method."""
        self.validator.assert_valid(
            method_name="getSigner",
            parameter_name="data",
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name="getSigner",
            parameter_name="signature",
            argument_value=signature,
        )
        return (data, signature)

    def call(
        self,
        data: StructsBridgeRequestData,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data, signature).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        data: StructsBridgeRequestData,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        data: StructsBridgeRequestData,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: StructsBridgeRequestData,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data, signature) = self.validate_and_normalize_inputs(data, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data, signature).estimateGas(
            tx_params.as_dict()
        )


class InitializeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class NextUserTransferIndexesMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the nextUserTransferIndexes method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the nextUserTransferIndexes method."""
        self.validator.assert_valid(
            method_name="nextUserTransferIndexes",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class OperatorHasMinimumWeightMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the operatorHasMinimumWeight method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str):
        """Validate the inputs to the operatorHasMinimumWeight method."""
        self.validator.assert_valid(
            method_name="operatorHasMinimumWeight",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return operator

    def call(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(operator).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).transact(tx_params.as_dict())

    def build_transaction(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator) = self.validate_and_normalize_inputs(operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator).estimateGas(
            tx_params.as_dict()
        )


class OperatorResponsesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the operatorResponses method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: int):
        """Validate the inputs to the operatorResponses method."""
        self.validator.assert_valid(
            method_name="operatorResponses",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="operatorResponses",
            parameter_name="index_1",
            argument_value=index_1,
        )
        # safeguard against fractional inputs
        index_1 = int(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class OwnerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class PublishAttestationMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the publishAttestation method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, attestation: Union[bytes, str], bridge_request_id: int
    ):
        """Validate the inputs to the publishAttestation method."""
        self.validator.assert_valid(
            method_name="publishAttestation",
            parameter_name="attestation",
            argument_value=attestation,
        )
        self.validator.assert_valid(
            method_name="publishAttestation",
            parameter_name="_bridgeRequestId",
            argument_value=bridge_request_id,
        )
        # safeguard against fractional inputs
        bridge_request_id = int(bridge_request_id)
        return (attestation, bridge_request_id)

    def call(
        self,
        attestation: Union[bytes, str],
        bridge_request_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (attestation, bridge_request_id) = self.validate_and_normalize_inputs(
            attestation, bridge_request_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(attestation, bridge_request_id).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        attestation: Union[bytes, str],
        bridge_request_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (attestation, bridge_request_id) = self.validate_and_normalize_inputs(
            attestation, bridge_request_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            attestation, bridge_request_id
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        attestation: Union[bytes, str],
        bridge_request_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (attestation, bridge_request_id) = self.validate_and_normalize_inputs(
            attestation, bridge_request_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            attestation, bridge_request_id
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        attestation: Union[bytes, str],
        bridge_request_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (attestation, bridge_request_id) = self.validate_and_normalize_inputs(
            attestation, bridge_request_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            attestation, bridge_request_id
        ).estimateGas(tx_params.as_dict())


class RegisterOperatorToAvsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the registerOperatorToAVS method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        operator: str,
        operator_signature: ISignatureUtilsSignatureWithSaltAndExpiry,
    ):
        """Validate the inputs to the registerOperatorToAVS method."""
        self.validator.assert_valid(
            method_name="registerOperatorToAVS",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="registerOperatorToAVS",
            parameter_name="operatorSignature",
            argument_value=operator_signature,
        )
        return (operator, operator_signature)

    def call(
        self,
        operator: str,
        operator_signature: ISignatureUtilsSignatureWithSaltAndExpiry,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, operator_signature) = self.validate_and_normalize_inputs(
            operator, operator_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator, operator_signature).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        operator: str,
        operator_signature: ISignatureUtilsSignatureWithSaltAndExpiry,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator, operator_signature) = self.validate_and_normalize_inputs(
            operator, operator_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, operator_signature).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        operator: str,
        operator_signature: ISignatureUtilsSignatureWithSaltAndExpiry,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, operator_signature) = self.validate_and_normalize_inputs(
            operator, operator_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, operator_signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        operator_signature: ISignatureUtilsSignatureWithSaltAndExpiry,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator, operator_signature) = self.validate_and_normalize_inputs(
            operator, operator_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, operator_signature
        ).estimateGas(tx_params.as_dict())


class ReleaseFundsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the releaseFunds method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        signatures: List[Union[bytes, str]],
        data: StructsBridgeRequestData,
    ):
        """Validate the inputs to the releaseFunds method."""
        self.validator.assert_valid(
            method_name="releaseFunds",
            parameter_name="signatures",
            argument_value=signatures,
        )
        self.validator.assert_valid(
            method_name="releaseFunds",
            parameter_name="data",
            argument_value=data,
        )
        return (signatures, data)

    def call(
        self,
        signatures: List[Union[bytes, str]],
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (signatures, data) = self.validate_and_normalize_inputs(
            signatures, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(signatures, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        signatures: List[Union[bytes, str]],
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (signatures, data) = self.validate_and_normalize_inputs(
            signatures, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(signatures, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        signatures: List[Union[bytes, str]],
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (signatures, data) = self.validate_and_normalize_inputs(
            signatures, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(signatures, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        signatures: List[Union[bytes, str]],
        data: StructsBridgeRequestData,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (signatures, data) = self.validate_and_normalize_inputs(
            signatures, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(signatures, data).estimateGas(
            tx_params.as_dict()
        )


class RenounceOwnershipMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the renounceOwnership method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class SetAvsRewardMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setAVSReward method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, avs_reward: int):
        """Validate the inputs to the setAVSReward method."""
        self.validator.assert_valid(
            method_name="setAVSReward",
            parameter_name="_AVSReward",
            argument_value=avs_reward,
        )
        # safeguard against fractional inputs
        avs_reward = int(avs_reward)
        return avs_reward

    def call(
        self, avs_reward: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (avs_reward) = self.validate_and_normalize_inputs(avs_reward)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(avs_reward).call(tx_params.as_dict())

    def send_transaction(
        self, avs_reward: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (avs_reward) = self.validate_and_normalize_inputs(avs_reward)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(avs_reward).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, avs_reward: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (avs_reward) = self.validate_and_normalize_inputs(avs_reward)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(avs_reward).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, avs_reward: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (avs_reward) = self.validate_and_normalize_inputs(avs_reward)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(avs_reward).estimateGas(
            tx_params.as_dict()
        )


class SetBridgeFeeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setBridgeFee method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, bridge_fee: int):
        """Validate the inputs to the setBridgeFee method."""
        self.validator.assert_valid(
            method_name="setBridgeFee",
            parameter_name="_bridgeFee",
            argument_value=bridge_fee,
        )
        # safeguard against fractional inputs
        bridge_fee = int(bridge_fee)
        return bridge_fee

    def call(
        self, bridge_fee: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bridge_fee) = self.validate_and_normalize_inputs(bridge_fee)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(bridge_fee).call(tx_params.as_dict())

    def send_transaction(
        self, bridge_fee: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bridge_fee) = self.validate_and_normalize_inputs(bridge_fee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bridge_fee).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, bridge_fee: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (bridge_fee) = self.validate_and_normalize_inputs(bridge_fee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bridge_fee).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, bridge_fee: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (bridge_fee) = self.validate_and_normalize_inputs(bridge_fee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bridge_fee).estimateGas(
            tx_params.as_dict()
        )


class SetCrankGasCostMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setCrankGasCost method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, crank_gas_cost: int):
        """Validate the inputs to the setCrankGasCost method."""
        self.validator.assert_valid(
            method_name="setCrankGasCost",
            parameter_name="_crankGasCost",
            argument_value=crank_gas_cost,
        )
        # safeguard against fractional inputs
        crank_gas_cost = int(crank_gas_cost)
        return crank_gas_cost

    def call(
        self, crank_gas_cost: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (crank_gas_cost) = self.validate_and_normalize_inputs(crank_gas_cost)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(crank_gas_cost).call(tx_params.as_dict())

    def send_transaction(
        self, crank_gas_cost: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (crank_gas_cost) = self.validate_and_normalize_inputs(crank_gas_cost)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(crank_gas_cost).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, crank_gas_cost: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (crank_gas_cost) = self.validate_and_normalize_inputs(crank_gas_cost)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(crank_gas_cost).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, crank_gas_cost: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (crank_gas_cost) = self.validate_and_normalize_inputs(crank_gas_cost)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(crank_gas_cost).estimateGas(
            tx_params.as_dict()
        )


class StakeRegistryMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stakeRegistry method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class TransferOwnershipMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transferOwnership method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the transferOwnership method."""
        self.validator.assert_valid(
            method_name="transferOwnership",
            parameter_name="newOwner",
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return new_owner

    def call(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params.as_dict())

    def send_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(
            tx_params.as_dict()
        )


class UpdateAvsMetadataUriMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the updateAVSMetadataURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, metadata_uri: str):
        """Validate the inputs to the updateAVSMetadataURI method."""
        self.validator.assert_valid(
            method_name="updateAVSMetadataURI",
            parameter_name="_metadataURI",
            argument_value=metadata_uri,
        )
        return metadata_uri

    def call(
        self, metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (metadata_uri) = self.validate_and_normalize_inputs(metadata_uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(metadata_uri).call(tx_params.as_dict())

    def send_transaction(
        self, metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (metadata_uri) = self.validate_and_normalize_inputs(metadata_uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(metadata_uri).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (metadata_uri) = self.validate_and_normalize_inputs(metadata_uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(metadata_uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (metadata_uri) = self.validate_and_normalize_inputs(metadata_uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(metadata_uri).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class BridgeServiceManager:
    """Wrapper class for BridgeServiceManager Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    avs_reward: AvsRewardMethod
    """Constructor-initialized instance of
    :class:`AvsRewardMethod`.
    """

    release_funds_: ReleaseFunds_Method
    """Constructor-initialized instance of
    :class:`ReleaseFunds_Method`.
    """

    avs_directory: AvsDirectoryMethod
    """Constructor-initialized instance of
    :class:`AvsDirectoryMethod`.
    """

    bridge: BridgeMethod
    """Constructor-initialized instance of
    :class:`BridgeMethod`.
    """

    bridge_fee: BridgeFeeMethod
    """Constructor-initialized instance of
    :class:`BridgeFeeMethod`.
    """

    bridge_request_weights: BridgeRequestWeightsMethod
    """Constructor-initialized instance of
    :class:`BridgeRequestWeightsMethod`.
    """

    bridge_requests: BridgeRequestsMethod
    """Constructor-initialized instance of
    :class:`BridgeRequestsMethod`.
    """

    challenge_attestation: ChallengeAttestationMethod
    """Constructor-initialized instance of
    :class:`ChallengeAttestationMethod`.
    """

    crank_gas_cost: CrankGasCostMethod
    """Constructor-initialized instance of
    :class:`CrankGasCostMethod`.
    """

    create_avs_rewards_submission: CreateAvsRewardsSubmissionMethod
    """Constructor-initialized instance of
    :class:`CreateAvsRewardsSubmissionMethod`.
    """

    current_bridge_request_id: CurrentBridgeRequestIdMethod
    """Constructor-initialized instance of
    :class:`CurrentBridgeRequestIdMethod`.
    """

    deregister_operator_from_avs: DeregisterOperatorFromAvsMethod
    """Constructor-initialized instance of
    :class:`DeregisterOperatorFromAvsMethod`.
    """

    eip712_domain: Eip712DomainMethod
    """Constructor-initialized instance of
    :class:`Eip712DomainMethod`.
    """

    get_digest: GetDigestMethod
    """Constructor-initialized instance of
    :class:`GetDigestMethod`.
    """

    get_operator_restaked_strategies: GetOperatorRestakedStrategiesMethod
    """Constructor-initialized instance of
    :class:`GetOperatorRestakedStrategiesMethod`.
    """

    get_operator_weight: GetOperatorWeightMethod
    """Constructor-initialized instance of
    :class:`GetOperatorWeightMethod`.
    """

    get_restakeable_strategies: GetRestakeableStrategiesMethod
    """Constructor-initialized instance of
    :class:`GetRestakeableStrategiesMethod`.
    """

    get_signer: GetSignerMethod
    """Constructor-initialized instance of
    :class:`GetSignerMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    next_user_transfer_indexes: NextUserTransferIndexesMethod
    """Constructor-initialized instance of
    :class:`NextUserTransferIndexesMethod`.
    """

    operator_has_minimum_weight: OperatorHasMinimumWeightMethod
    """Constructor-initialized instance of
    :class:`OperatorHasMinimumWeightMethod`.
    """

    operator_responses: OperatorResponsesMethod
    """Constructor-initialized instance of
    :class:`OperatorResponsesMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    publish_attestation: PublishAttestationMethod
    """Constructor-initialized instance of
    :class:`PublishAttestationMethod`.
    """

    register_operator_to_avs: RegisterOperatorToAvsMethod
    """Constructor-initialized instance of
    :class:`RegisterOperatorToAvsMethod`.
    """

    release_funds: ReleaseFundsMethod
    """Constructor-initialized instance of
    :class:`ReleaseFundsMethod`.
    """

    renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    set_avs_reward: SetAvsRewardMethod
    """Constructor-initialized instance of
    :class:`SetAvsRewardMethod`.
    """

    set_bridge_fee: SetBridgeFeeMethod
    """Constructor-initialized instance of
    :class:`SetBridgeFeeMethod`.
    """

    set_crank_gas_cost: SetCrankGasCostMethod
    """Constructor-initialized instance of
    :class:`SetCrankGasCostMethod`.
    """

    stake_registry: StakeRegistryMethod
    """Constructor-initialized instance of
    :class:`StakeRegistryMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    update_avs_metadata_uri: UpdateAvsMetadataUriMethod
    """Constructor-initialized instance of
    :class:`UpdateAvsMetadataUriMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: BridgeServiceManagerValidator = None,
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
            validator = BridgeServiceManagerValidator(
                web3_or_provider, contract_address
            )

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

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=BridgeServiceManager.abi(),
        ).functions

        self.avs_reward = AvsRewardMethod(
            web3_or_provider, contract_address, functions.AVSReward
        )

        self.release_funds_ = ReleaseFunds_Method(
            web3_or_provider,
            contract_address,
            functions._releaseFunds,
            validator,
        )

        self.avs_directory = AvsDirectoryMethod(
            web3_or_provider, contract_address, functions.avsDirectory
        )

        self.bridge = BridgeMethod(
            web3_or_provider, contract_address, functions.bridge, validator
        )

        self.bridge_fee = BridgeFeeMethod(
            web3_or_provider, contract_address, functions.bridgeFee
        )

        self.bridge_request_weights = BridgeRequestWeightsMethod(
            web3_or_provider,
            contract_address,
            functions.bridgeRequestWeights,
            validator,
        )

        self.bridge_requests = BridgeRequestsMethod(
            web3_or_provider,
            contract_address,
            functions.bridgeRequests,
            validator,
        )

        self.challenge_attestation = ChallengeAttestationMethod(
            web3_or_provider,
            contract_address,
            functions.challengeAttestation,
            validator,
        )

        self.crank_gas_cost = CrankGasCostMethod(
            web3_or_provider, contract_address, functions.crankGasCost
        )

        self.create_avs_rewards_submission = CreateAvsRewardsSubmissionMethod(
            web3_or_provider,
            contract_address,
            functions.createAVSRewardsSubmission,
            validator,
        )

        self.current_bridge_request_id = CurrentBridgeRequestIdMethod(
            web3_or_provider,
            contract_address,
            functions.currentBridgeRequestId,
        )

        self.deregister_operator_from_avs = DeregisterOperatorFromAvsMethod(
            web3_or_provider,
            contract_address,
            functions.deregisterOperatorFromAVS,
            validator,
        )

        self.eip712_domain = Eip712DomainMethod(
            web3_or_provider, contract_address, functions.eip712Domain
        )

        self.get_digest = GetDigestMethod(
            web3_or_provider, contract_address, functions.getDigest, validator
        )

        self.get_operator_restaked_strategies = (
            GetOperatorRestakedStrategiesMethod(
                web3_or_provider,
                contract_address,
                functions.getOperatorRestakedStrategies,
                validator,
            )
        )

        self.get_operator_weight = GetOperatorWeightMethod(
            web3_or_provider,
            contract_address,
            functions.getOperatorWeight,
            validator,
        )

        self.get_restakeable_strategies = GetRestakeableStrategiesMethod(
            web3_or_provider,
            contract_address,
            functions.getRestakeableStrategies,
        )

        self.get_signer = GetSignerMethod(
            web3_or_provider, contract_address, functions.getSigner, validator
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize
        )

        self.next_user_transfer_indexes = NextUserTransferIndexesMethod(
            web3_or_provider,
            contract_address,
            functions.nextUserTransferIndexes,
            validator,
        )

        self.operator_has_minimum_weight = OperatorHasMinimumWeightMethod(
            web3_or_provider,
            contract_address,
            functions.operatorHasMinimumWeight,
            validator,
        )

        self.operator_responses = OperatorResponsesMethod(
            web3_or_provider,
            contract_address,
            functions.operatorResponses,
            validator,
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.publish_attestation = PublishAttestationMethod(
            web3_or_provider,
            contract_address,
            functions.publishAttestation,
            validator,
        )

        self.register_operator_to_avs = RegisterOperatorToAvsMethod(
            web3_or_provider,
            contract_address,
            functions.registerOperatorToAVS,
            validator,
        )

        self.release_funds = ReleaseFundsMethod(
            web3_or_provider,
            contract_address,
            functions.releaseFunds,
            validator,
        )

        self.renounce_ownership = RenounceOwnershipMethod(
            web3_or_provider, contract_address, functions.renounceOwnership
        )

        self.set_avs_reward = SetAvsRewardMethod(
            web3_or_provider,
            contract_address,
            functions.setAVSReward,
            validator,
        )

        self.set_bridge_fee = SetBridgeFeeMethod(
            web3_or_provider,
            contract_address,
            functions.setBridgeFee,
            validator,
        )

        self.set_crank_gas_cost = SetCrankGasCostMethod(
            web3_or_provider,
            contract_address,
            functions.setCrankGasCost,
            validator,
        )

        self.stake_registry = StakeRegistryMethod(
            web3_or_provider, contract_address, functions.stakeRegistry
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

        self.update_avs_metadata_uri = UpdateAvsMetadataUriMethod(
            web3_or_provider,
            contract_address,
            functions.updateAVSMetadataURI,
            validator,
        )

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
                abi=BridgeServiceManager.abi(),
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
                abi=BridgeServiceManager.abi(),
            )
            .events.BridgeRequest()
            .processReceipt(tx_receipt)
        )

    def get_eip712_domain_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for EIP712DomainChanged event.

        :param tx_hash: hash of transaction emitting EIP712DomainChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=BridgeServiceManager.abi(),
            )
            .events.EIP712DomainChanged()
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
                abi=BridgeServiceManager.abi(),
            )
            .events.FundsReleased()
            .processReceipt(tx_receipt)
        )

    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=BridgeServiceManager.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_ownership_transferred_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnershipTransferred event.

        :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=BridgeServiceManager.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    def get_rewards_initiator_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RewardsInitiatorUpdated event.

        :param tx_hash: hash of transaction emitting RewardsInitiatorUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=BridgeServiceManager.abi(),
            )
            .events.RewardsInitiatorUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"type":"constructor","inputs":[{"name":"_avsDirectory","type":"address","internalType":"address"},{"name":"_stakeRegistry","type":"address","internalType":"address"},{"name":"_rewardsCoordinator","type":"address","internalType":"address"},{"name":"_delegationManager","type":"address","internalType":"address"},{"name":"_crankGasCost","type":"uint256","internalType":"uint256"},{"name":"_AVSReward","type":"uint256","internalType":"uint256"},{"name":"_bridgeFee","type":"uint256","internalType":"uint256"},{"name":"_name","type":"string","internalType":"string"},{"name":"_version","type":"string","internalType":"string"}],"stateMutability":"nonpayable"},{"type":"receive","stateMutability":"payable"},{"type":"function","name":"AVSReward","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"_releaseFunds","inputs":[{"name":"data","type":"bytes","internalType":"bytes"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"avsDirectory","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"bridge","inputs":[{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"bridgeFee","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"bridgeRequestWeights","inputs":[{"name":"index_0","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"bridgeRequests","inputs":[{"name":"index_0","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"challengeAttestation","inputs":[{"name":"fraudulentSignature","type":"bytes","internalType":"bytes"},{"name":"fraudulentBridgeRequest","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"crankGasCost","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"createAVSRewardsSubmission","inputs":[{"name":"rewardsSubmissions","type":"tuple[]","internalType":"struct IRewardsCoordinator.RewardsSubmission[]","components":[{"name":"strategiesAndMultipliers","type":"tuple[]","internalType":"struct IRewardsCoordinator.StrategyAndMultiplier[]","components":[{"name":"strategy","type":"address","internalType":"contract IStrategy"},{"name":"multiplier","type":"uint96","internalType":"uint96"}]},{"name":"token","type":"address","internalType":"contract IERC20"},{"name":"amount","type":"uint256","internalType":"uint256"},{"name":"startTimestamp","type":"uint32","internalType":"uint32"},{"name":"duration","type":"uint32","internalType":"uint32"}]}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"currentBridgeRequestId","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"deregisterOperatorFromAVS","inputs":[{"name":"operator","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"eip712Domain","inputs":[],"outputs":[{"name":"fields","type":"bytes1","internalType":"bytes1"},{"name":"name","type":"string","internalType":"string"},{"name":"version","type":"string","internalType":"string"},{"name":"chainId","type":"uint256","internalType":"uint256"},{"name":"verifyingContract","type":"address","internalType":"address"},{"name":"salt","type":"bytes32","internalType":"bytes32"},{"name":"extensions","type":"uint256[]","internalType":"uint256[]"}],"stateMutability":"view"},{"type":"function","name":"getDigest","inputs":[{"name":"data","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]}],"outputs":[{"name":"","type":"bytes32","internalType":"bytes32"}],"stateMutability":"view"},{"type":"function","name":"getOperatorRestakedStrategies","inputs":[{"name":"_operator","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"address[]","internalType":"address[]"}],"stateMutability":"view"},{"type":"function","name":"getOperatorWeight","inputs":[{"name":"operator","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getRestakeableStrategies","inputs":[],"outputs":[{"name":"","type":"address[]","internalType":"address[]"}],"stateMutability":"view"},{"type":"function","name":"getSigner","inputs":[{"name":"data","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]},{"name":"signature","type":"bytes","internalType":"bytes"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"initialize","inputs":[],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"nextUserTransferIndexes","inputs":[{"name":"index_0","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"operatorHasMinimumWeight","inputs":[{"name":"operator","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"view"},{"type":"function","name":"operatorResponses","inputs":[{"name":"index_0","type":"address","internalType":"address"},{"name":"index_1","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"view"},{"type":"function","name":"owner","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"publishAttestation","inputs":[{"name":"attestation","type":"bytes","internalType":"bytes"},{"name":"_bridgeRequestId","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"registerOperatorToAVS","inputs":[{"name":"operator","type":"address","internalType":"address"},{"name":"operatorSignature","type":"tuple","internalType":"struct ISignatureUtils.SignatureWithSaltAndExpiry","components":[{"name":"signature","type":"bytes","internalType":"bytes"},{"name":"salt","type":"bytes32","internalType":"bytes32"},{"name":"expiry","type":"uint256","internalType":"uint256"}]}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"releaseFunds","inputs":[{"name":"signatures","type":"bytes[]","internalType":"bytes[]"},{"name":"data","type":"tuple","internalType":"struct Structs.BridgeRequestData","components":[{"name":"user","type":"address","internalType":"address"},{"name":"tokenAddress","type":"address","internalType":"address"},{"name":"amountIn","type":"uint256","internalType":"uint256"},{"name":"amountOut","type":"uint256","internalType":"uint256"},{"name":"destinationVault","type":"address","internalType":"address"},{"name":"destinationAddress","type":"address","internalType":"address"},{"name":"transferIndex","type":"uint256","internalType":"uint256"}]}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"renounceOwnership","inputs":[],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setAVSReward","inputs":[{"name":"_AVSReward","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setBridgeFee","inputs":[{"name":"_bridgeFee","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setCrankGasCost","inputs":[{"name":"_crankGasCost","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"stakeRegistry","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"transferOwnership","inputs":[{"name":"newOwner","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"updateAVSMetadataURI","inputs":[{"name":"_metadataURI","type":"string","internalType":"string"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"event","name":"AVSAttestation","inputs":[{"name":"attestation","type":"bytes","indexed":true,"internalType":"bytes"},{"name":"bridgeRequestId","type":"uint256","indexed":true,"internalType":"uint256"},{"name":"operatorWeight","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"BridgeRequest","inputs":[{"name":"user","type":"address","indexed":true,"internalType":"address"},{"name":"tokenAddress","type":"address","indexed":true,"internalType":"address"},{"name":"bridgeRequestId","type":"uint256","indexed":true,"internalType":"uint256"},{"name":"amountIn","type":"uint256","indexed":false,"internalType":"uint256"},{"name":"amountOut","type":"uint256","indexed":false,"internalType":"uint256"},{"name":"destinationVault","type":"address","indexed":false,"internalType":"address"},{"name":"destinationAddress","type":"address","indexed":false,"internalType":"address"},{"name":"transferIndex","type":"uint256","indexed":false,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"EIP712DomainChanged","inputs":[],"anonymous":false},{"type":"event","name":"FundsReleased","inputs":[{"name":"destinationVault","type":"address","indexed":true,"internalType":"address"},{"name":"destinationAddress","type":"address","indexed":true,"internalType":"address"},{"name":"amountOut","type":"uint256","indexed":true,"internalType":"uint256"}],"anonymous":false},{"type":"event","name":"Initialized","inputs":[{"name":"version","type":"uint8","indexed":false,"internalType":"uint8"}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"name":"previousOwner","type":"address","indexed":true,"internalType":"address"},{"name":"newOwner","type":"address","indexed":true,"internalType":"address"}],"anonymous":false},{"type":"event","name":"RewardsInitiatorUpdated","inputs":[{"name":"prevRewardsInitiator","type":"address","indexed":false,"internalType":"address"},{"name":"newRewardsInitiator","type":"address","indexed":false,"internalType":"address"}],"anonymous":false},{"type":"error","name":"ECDSAInvalidSignature","inputs":[]},{"type":"error","name":"ECDSAInvalidSignatureLength","inputs":[{"name":"length","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"ECDSAInvalidSignatureS","inputs":[{"name":"s","type":"bytes32","internalType":"bytes32"}]},{"type":"error","name":"InvalidShortString","inputs":[]},{"type":"error","name":"ReentrancyGuardReentrantCall","inputs":[]},{"type":"error","name":"StringTooLong","inputs":[{"name":"str","type":"string","internalType":"string"}]}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
