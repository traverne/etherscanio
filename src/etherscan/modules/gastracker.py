from .base import Module


class GasTracker(Module):
    module = "gastracker"

    def estimate_confirmation_time(self, gas_price: int):
        payload = {"action": "gasestimate", "gasprice": gas_price}

        self.modulize(payload)
        return self.client.request(payload)

    def get_gas_oracle(self):
        payload = {"action": "gasoracle"}

        self.modulize(payload)
        return self.client.request(payload)
