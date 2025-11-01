from .base import Module


class Accounts(Module):
    module = "account"

    def get_native_balance(self, address: str | list[str], tag: str = "latest"):
        self.assertions.tag(tag)

        if isinstance(address, list):
            action = "balancemulti"
            [self.assertions.address(addr) for addr in address]
            address = self.sequenced(address)

        else:
            action = "balance"
            self.assertions.address(address)

        payload = {"action": action, "address": address, "tag": tag}

        self.modulize(payload)
        return self.client.request(payload)

    def get_historical_native_balance(self, address: str, block_number: int):
        self.assertions.address(address)

        payload = {
            "action": "balancehistory",
            "address": address,
            "blockno": block_number,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_normal_transactions(
        self,
        address: str,
        start_block: int,
        end_block: int,
        page: int,
        offset: int,
        sort: str,
    ):
        self.assertions.address(address)
        self.assertions.sorting(sort)

        payload = {
            "action": "txlist",
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_ERC20_transfers(
        self,
        address: str,
        contract_address: str,
        start_block: int,
        end_block: int,
        page: int,
        offset: int,
        sort: str,
    ):
        self.assertions.address(address)
        self.assertions.address(contract_address)
        self.assertions.sorting(sort)

        payload = {
            "action": "tokentx",
            "address": address,
            "contractaddress": contract_address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_erc721_transfers(
        self,
        address: str,
        contract_address: str,
        start_block: int,
        end_block: int,
        page: int,
        offset: int,
        sort: str,
    ):
        self.assertions.address(address)
        self.assertions.address(contract_address)
        self.assertions.sorting(sort)

        payload = {
            "action": "tokennfttx",
            "address": address,
            "contractaddress": contract_address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_erc1155_transfers(
        self,
        address: str,
        contract_address: str,
        start_block: int,
        end_block: int,
        page: int,
        offset: int,
        sort: str,
    ):
        self.assertions.address(address)
        self.assertions.address(contract_address)
        self.assertions.sorting(sort)

        payload = {
            "action": "token1155tx",
            "address": address,
            "contractaddress": contract_address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_internal_txs_by_block_range(
        self, start_block: int, end_block: int, page: int, offset: int, sort: str
    ):
        self.assertions.sorting(sort)

        payload = {
            "action": "txlistinternal",
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_internal_txs_by_txhash(self, tx_hash: str):
        self.assertions.transaction(tx_hash)

        payload = {"action": "txlistinternal", "txhash": tx_hash}

        self.modulize(payload)
        return self.client.request(payload)

    def get_validated_blocks(
        self, address: str, block_type: str, page: int, offset: int
    ):
        self.assertions.address(address)

        payload = {
            "action": "getminedblocks",
            "address": address,
            "blocktype": block_type,
            "page": page,
            "offset": offset,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_beacon_chain_withdrawals(
        self,
        address: str,
        start_block: int,
        end_block: int,
        page: int,
        offset: int,
        sort: str,
    ):
        self.assertions.address(address)
        self.assertions.sorting(sort)

        payload = {
            "action": "txsBeaconWithdrawal",
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)
