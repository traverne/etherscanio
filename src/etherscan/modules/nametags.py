from .base import Module


class Nametags(Module):
    module = "nametag"

    def get_nametag(self, address: str):
        self.assertions.address(address)

        payload = {"action": "getaddresstag", "address": address}

        self.modulize(payload)
        return self.client.request(address)
