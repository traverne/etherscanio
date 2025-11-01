from .base import Module


class Logs(Module):
    module = "logs"

    def get_event_logs(
        self,
        address: str,
        from_block: int,
        to_block: int,
        page: int = 1,
        offset: int = 1000,
    ):
        self.assertions.address(address)
        self.assertions.limits(offset, 1000)

        payload = {
            "module": "logs",
            "action": "getLogs",
            "address": address,
            "fromBlock": from_block,
            "toBlock": to_block,
            "page": page,
            "offset": offset,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_event_logs_by_topics(
        self,
        from_block: int,
        to_block: int,
        topic0: str,
        topic1: str = chr(0x20),
        topic2: str = chr(0x20),
        topic3: str = chr(0x20),
        topic0_1_opr: str = "and",
        topic1_2_opr: str = "and",
        topic2_3_opr: str = "and",
        topic0_2_opr: str = "and",
        topic0_3_opr: str = "and",
        topic1_3_opr: str = "and",
        page: int = 1,
        offset: int = 1000,
    ):
        self.assertions.limits(offset, 1000)

        payload = {
            "module": "logs",
            "action": "getLogs",
            "fromBlock": from_block,
            "toBlock": to_block,
            "page": page,
            "offset": offset,
        }

        topics = {
            "topic0": topic0,
            "topic1": topic1,
            "topic2": topic2,
            "topic3": topic3,
            "topic0_1_opr": topic0_1_opr,
            "topic1_2_opr": topic1_2_opr,
            "topic2_3_opr": topic2_3_opr,
            "topic0_2_opr": topic0_2_opr,
            "topic0_3_opr": topic0_3_opr,
            "topic1_3_opr": topic1_3_opr,
        }

        for k, v in topics.items():
            if v:
                payload[k] = v

        self.modulize(payload)
        return self.client.request(payload)

    def get_event_logs_by(
        self,
        address: str,
        from_block: int,
        to_block: int,
        topic0: str,
        topic1: str = chr(0x20),
        topic0_1_opr: str = "and",
        page: int = 1,
        offset: int = 1000,
    ):
        self.assertions.address(address)
        self.assertions.limits(offset, 1000)

        payload = {
            "module": "logs",
            "action": "getLogs",
            "address": address,
            "fromBlock": from_block,
            "toBlock": to_block,
            "page": page,
            "offset": offset,
        }

        topics = {
            "topic0": topic0,
            "topic1": topic1,
            "topic0_1_opr": topic0_1_opr,
        }

        for k, v in topics.items():
            if v:
                payload[k] = v

        self.modulize(payload)
        return self.client.request(payload)
