from eth_account.signers.local import LocalAccount


class AVSOperator:
    def __init__(self, signer: LocalAccount):
        self.signer = signer


if __name__ == "__main__":
    print("HELLO")
