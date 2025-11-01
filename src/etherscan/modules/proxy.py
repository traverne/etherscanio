from .base import Module


class Proxy(Module):
    module = "proxy"

    def get_block_number(self):
        payload = {"action": "eth_blockNumber"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_block(self, tag: str, boolean: bool = False):
        self.assertions.tag(tag)

        payload = {
            "action": "eth_getBlockByNumber",
            "tag": tag,
            "boolean": str(boolean).lower(),
        }

        self.modulize(payload)
        return self.client.request(payload)

    # TODO: FROM eth_getUncleByBlockNumberAndIndex
    def get_uncle(self, tag: str, index: str):
        self.assertions.tag(tag)

        payload = {
            "action": "eth_getUncleByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_block_transaction_count(self, tag: str):
        self.assertions.tag(tag)

        payload = {"action": "eth_getBlockTransactionCountByNumber", "tag": tag}

        self.modulize(payload)
        return self.client.request(payload)

    def get_transaction(self, tx_hash: str):
        self.assertions.transaction(tx_hash)

        payload = {"action": "eth_getTransactionByHash", "txhash": tx_hash}

        self.modulize(payload)
        return self.client.request(payload)

    def get_transaction_by_index(self, tag: str, index: str):
        self.assertions.tag(tag)

        payload = {
            "action": "eth_getTransactionByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_transaction_count(self, address: str, tag: str = "latest"):
        self.assertions.address(address)
        self.assertions.tag(tag)

        payload = {"action": "eth_getTransactionCount", "address": address}

        self.modulize(payload)
        return self.client.request(payload)

    def send_raw_transaction(self, transaction: str):
        payload = {"action": "eth_sendRawTransaction", "hex": transaction}

        self.modulize(payload)
        return self.client.request(payload)

    def get_transaction_receipt(self, tx_hash: str):
        self.assertions.transaction(tx_hash)

        payload = {"action": "eth_getTransactionReceipt", "txhash": tx_hash}

        self.modulize(payload)
        return self.client.request(payload)

    def call(self, to: str, data: str, tag: str = "latest"):
        self.assertions.address(to)
        self.assertions.tag(tag)

        payload = {"action": "eth_call", "to": to, "data": data, "tag": tag}

        self.modulize(payload)
        return self.client.request(payload)

    def get_code(self, contract_address: str, tag: str = "latest"):
        self.assertions.address(contract_address)
        self.assertions.tag(tag)

        payload = {"action": "eth_getCode", "address": contract_address, "tag": tag}

        self.modulize(payload)
        return self.client.request(payload)

    def get_storage_at(self, contract_address: str, position: str, tag: str = "latest"):
        self.assertions.address(contract_address)
        self.assertions.tag(tag)

        payload = {
            "action": "eth_getStorageAt",
            "address": contract_address,
            "position": position,
            "tag": tag,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_gas_price(self):
        payload = {"action": "eth_gasPrice"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_estimate_gas(
        self, to: str, data: str, value: str, gas_price: str, gas: str
    ):
        self.assertions.address(to)

        payload = {
            "action": "eth_estimateGas",
            "to": to,
            "data": data,
            "value": value,
            "gasPrice": gas_price,
            "gas": gas,
        }

        self.modulize(payload)
        return self.client.request(payload)
