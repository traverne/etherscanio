from .base import Module


class Tokens(Module):
    module = "tokens"

    def __init__(self, client):
        super().__init__(client)

        self.ERC20 = Tokens._ERC20(self)
        self.ERC721 = Tokens._ERC721(self)

    class _ERC20:
        def __init__(self, parent):
            self.tokens = parent

        def get_total_supply(self, contract_address: str):
            self.tokens.assertions.address(contract_address)

            payload = {"action": "tokensupply", "contractaddress": contract_address}

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_account_balance(
            self, contract_address: str, user_address: str, tag: str = "latest"
        ):
            self.tokens.assertions.address(contract_address)
            self.tokens.assertions.address(user_address)
            self.tokens.assertions.tag(tag)

            payload = {
                "action": "tokenbalance",
                "contractaddress": contract_address,
                "address": user_address,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_historical_total_supply(self, contract_address: str, block_number: int):
            self.tokens.assertions.address(contract_address)

            payload = {
                "action": "tokensupplyhistory",
                "contractaddress": contract_address,
                "blockno": block_number,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_historical_account_balance(
            self, contract_address: str, user_address: str, block_number: int
        ):
            self.tokens.assertions.address(contract_address)
            self.tokens.assertions.address(user_address)

            payload = {
                "action": "tokenbalancehistory",
                "contractaddress": contract_address,
                "address": user_address,
                "blockno": block_number,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_top_token_holders(self, contract_address: str, offset: int = 100):
            self.tokens.assertions.address(contract_address)
            self.tokens.assertions.limit(offset, 1_000)

            payload = {
                "action": "topholders",
                "contractaddress": contract_address,
                "offset": offset,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_token_holder_list(
            self, contract_address: str, page: int = 1, offset: int = 10
        ):
            self.tokens.assertions.address(contract_address)

            payload = {
                "action": "tokenholderlist",
                "contractaddress": contract_address,
                "page": page,
                "offset": offset,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_token_holder_count(self, contract_address: str):
            self.tokens.assertions.address(contract_address)

            payload = {
                "action": "tokenholdercount",
                "contractaddress": contract_address,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_token_information(self, contract_address: str):
            self.tokens.assertions.address(contract_address)

            payload = {"action": "tokeninfo", "contractaddress": contract_address}

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_address_token_holding(
            self, user_address: str, page: int = 1, offset: int = 100
        ):
            self.tokens.assertions.address(user_address)

            payload = {
                "action": "addresstokenbalance",
                "address": user_address,
                "page": page,
                "offset": offset,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

    class _ERC721:
        def __init__(self, parent):
            self.tokens = parent

        def get_address_token_holding(
            self, user_address: str, page: int = 1, offset: int = 100
        ):
            self.tokens.assertions.address(user_address)

            payload = {
                "action": "addresstokennftbalance",
                "address": user_address,
                "page": page,
                "offset": offset,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)

        def get_token_inventory(
            self,
            contract_address: str,
            user_address: str,
            page: int = 1,
            offset: int = 100,
        ):
            self.tokens.assertions.address(contract_address)
            self.tokens.assertions.address(user_address)

            payload = {
                "action": "addresstokennftinventory",
                "contractaddress": contract_address,
                "address": user_address,
                "page": page,
                "offset": offset,
            }

            self.tokens.modulize(payload)
            return self.tokens.client.request(payload)
