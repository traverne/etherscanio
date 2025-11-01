from .base import Module


class Transactions(Module):
    module = "transaction"

    def get_execution_status(self, tx_hash: str):
        self.assertions.transaction(tx_hash)

        payload = {"action": "getstatus", "txhash": tx_hash}

        self.modulize(payload)
        return self.client.request(payload)

    def get_transaction_receipt(self, tx_hash: str):
        self.assertions.transaction(tx_hash)

        payload = {"action": "gettxreceiptstatus", "txhash": tx_hash}

        self.modulize(payload)
        return self.client.request(payload)
