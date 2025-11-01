from .base import Module


class Contracts(Module):
    module = "contract"

    def get_contract_abi(self, address: str):
        self.assertions.address(address)

        payload = {"module": "contract", "action": "getabi", "address": address}

        self.modulize(payload)
        return self.client.request(payload)

    def get_source_code(self, address: str):
        self.assertions.address(address)

        payload = {"module": "contract", "action": "getsourcecode", "address": address}

        self.modulize(payload)
        response = self.client.request(payload)
        if response[0]["ABI"] == "Contract source code not verified":
            raise ValueError(f"Address {address} is not verified")

        return response

    def get_contract_creation(self, address: str | list[str]):
        if isinstance(address, str):
            address = [address]

        [self.assertions.address(addr) for addr in address]

        payload = {
            "module": "contract",
            "action": "getcontractcreation",
            "contractaddresses": self.sequenced(address),
        }

        self.modulize(payload)
        return self.client.request(payload)

    def verify_solidity_source_code(
        self,
        address: str,
        contract_name: str,
        code_format: str,
        source_code: str | list[dict],
        compiler_version: str,
        constructor_args: str = "",
    ):
        self.assertions.address(address)
        self.assertions.format(code_format)

        payload = {
            "module": "contract",
            "action": "verifysourcecode",
            "data": {
                "chainId": self.client.chain_id,
                "codeformat": code_format,
                "sourceCode": source_code,
                "contractaddress": address,
                "contractname": contract_name,
                "compilerversion": compiler_version,
            },
        }

        if constructor_args:
            payload["data"]["constructorArguments"] = constructor_args

        self.modulize(payload)
        return self.client.request(payload, "POST")

    def verify_proxy_contract(self, proxy_address: str, expected_impl: str = ""):
        self.assertions.address(proxy_address)
        if expected_impl:
            self.assertions.address(expected_impl)

        payload = {
            "module": "contract",
            "action": "verifyproxycontract",
            "address": proxy_address,
        }

        if expected_impl:
            payload["expectedimplementation"] = expected_impl

        self.modulize(payload)
        return self.client.request(payload)

    def get_verification_status(self, guid: str):
        payload = {"module": "contract", "action": "checkverifystatus", "guid": guid}

        self.modulize(payload)
        return self.client.request(payload)
