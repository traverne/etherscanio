import re
from ..exceptions import validate


class Module:
    module: str

    def __init__(self, client) -> None:
        self.client = client
        self.data = {"module": self.module}

    def modulize(self, payload: dict) -> None:
        payload.update(self.data)

    def sequenced(self, param: list[str]) -> str:
        return chr(0x2C).join(param)

    @staticmethod
    def is_valid_eth_addr(addr: str) -> bool:
        return bool(re.match(r"^0x[a-fA-F0-9]{40}$", addr))

    @staticmethod
    def is_valid_eth_txhash(tx_hash: str) -> bool:
        return bool(re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash))

    @staticmethod
    def is_valid_date(date: str) -> bool:
        return bool(re.match(r"^\d{4}-(0[1-9]|1[0-2])-([0-2]\d|3[01])$", date))

    @staticmethod
    def is_valid_hex(h: str) -> bool:
        return bool(re.fullmatch(r"0x[0-9a-fA-F]+", h))

    @staticmethod
    def is_valid_sort(sort: str) -> bool:
        return sort in ["asc", "desc"]

    @staticmethod
    def is_valid_client_type(client_type: str) -> bool:
        return client_type in ["geth", "parity"]

    @staticmethod
    def is_valid_sync_mode(sync_mode: str) -> bool:
        return sync_mode in ["default", "archive"]

    @staticmethod
    def is_valid_format(format: str) -> bool:
        return format in ["solidity-single-file", "standard-json-input"]

    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        if tag not in ["latest", "pending", "earliest"]:
            return Module.is_valid_hex(tag)

        return True

    class assertions:
        @staticmethod
        def address(x: str) -> None:
            validate(Module.is_valid_eth_addr(x), f"Invalid EVM address: {x}")

        @staticmethod
        def tag(x: str) -> None:
            validate(Module.is_valid_tag(x), f"Invalid EVM tag: {x}")

        @staticmethod
        def transaction(x: str) -> None:
            validate(Module.is_valid_eth_txhash(x), f"Invalid EVM transaction: {x}")

        @staticmethod
        def sorting(x: str) -> None:
            validate(Module.is_valid_sort(x), f"Invalid sorting method: {x}")

        @staticmethod
        def date(x: str) -> None:
            validate(Module.is_valid_date(x), f"Invalid date provided: {x}")

        @staticmethod
        def client(x: str) -> None:
            validate(Module.is_valid_client_type(x), f"Invalid client type: {x}")

        @staticmethod
        def sync(x: str) -> None:
            validate(Module.is_valid_sync_mode(x), f"Invalid sync mode: {x}")

        @staticmethod
        def format(x: str) -> None:
            validate(Module.is_valid_format(x), f"Invalid file format provided: {x}")

        @staticmethod
        def limits(x: int, y: int) -> None:
            validate(
                x > 0 and x <= y,
                f"Parameters exceeds API limits. Parameter passed: {x}; Method limit: {y}",
            )
