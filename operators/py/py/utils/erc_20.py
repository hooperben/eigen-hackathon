import json

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress
from web3 import Web3

erc20_abi = """
[
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
"""


def approve_token(web3: Web3, token_address: ChecksumAddress, destination_address: ChecksumAddress, amount_wei: int, signer: LocalAccount) -> str:
    # Load the ERC20 ABI
    abi = json.loads(erc20_abi)

    # Create a contract instance
    contract = web3.eth.contract(address=token_address, abi=abi)

    # Get the address from the private key
    account_address = signer.address

    # Build the transaction
    tx = contract.functions.approve(destination_address, amount_wei).build_transaction({
        'from': account_address,
        'nonce': web3.eth.get_transaction_count(account_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei')
    })

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, signer.key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Wait for the transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt.transactionHash.hex()
