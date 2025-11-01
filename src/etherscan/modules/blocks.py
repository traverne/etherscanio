from .base import Module


class Blocks(Module):
    module = "blocks"

    def get_block_rewards(self, block_number: int):
        payload = {"action": "getblockreward", "blockno": block_number}

        self.modulize(payload)
        return self.client.request(payload)

    def get_block_countdown(self, block_number: int):
        payload = {"action": "getblockcountdown", "blockno": block_number}

        self.modulize(payload)
        return self.client.request(payload)

    def get_block_number_by_timestamp(self, timestamp: int, closest: str = "after"):
        payload = {
            "action": "getblocknobytime",
            "timestamp": timestamp,
            "closest": closest,
        }

        self.modulize(payload)
        return self.client.request(payload)
