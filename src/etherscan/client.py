import re
import os
import httpx

from typing import Any

from .exceptions import validate
from .modules import (
    accounts,
    contracts,
    transactions,
    tokens,
    statistics,
    blocks,
    gastracker,
    proxy,
    logs,
    nametags,
)


class Etherscan:
    endpoint: str = "https://api.etherscan.io/v2/api"
    timeout: int = 10

    accounts: accounts.Accounts
    blocks: blocks.Blocks
    contracts: contracts.Contracts
    gastracker: gastracker.GasTracker
    logs: logs.Logs
    nametags: nametags.Nametags
    eth: proxy.Proxy
    statistics: statistics.Statistics
    tokens: tokens.Tokens
    transactions: transactions.Transactions

    def __init__(self, chain_id: int, api_key: str = chr(0x20)) -> None:
        validate(Etherscan.is_supported_chain(chain_id, api_key), "Chain not supported")

        if not api_key:
            api_key = os.environ.get("ETHERSCAN_API_KEY", chr(0x20))
            validate(
                len(api_key) > 0, "API key neither set in environment nor in instance"
            )

        validate(Etherscan.is_valid_api_key(api_key), "Invalid API key")

        self.client = httpx.Client(timeout=self.timeout)
        self.data = {"chainid": chain_id, "apiKey": api_key}

        self.accounts = accounts.Accounts(self)
        self.transactions = transactions.Transactions(self)
        self.statistics = statistics.Statistics(self)
        self.tokens = tokens.Tokens(self)
        self.blocks = blocks.Blocks(self)
        self.gastracker = gastracker.GasTracker(self)
        self.eth = proxy.Proxy(self)
        self.logs = logs.Logs(self)
        self.nametags = nametags.Nametags(self)
        self.contracts = contracts.Contracts(self)

    def request(self, payload: dict, method: str = "GET") -> Any:
        payload.update(self.data)
        response: httpx.Response

        if method == "GET":
            response = self.client.get(self.endpoint, params=payload)

        elif method == "POST":
            validate(bool(payload.get("data", False)), "[Internal] Payload error")

            data = payload["data"].copy()
            del payload["data"]

            response = self.client.post(self.endpoint, params=payload, json=data)
        else:
            validate(
                False,
                "[Internal] Invalid API request type",
            )
            return {}

        response.raise_for_status()
        result = response.json()

        validate(
            result["status"] == "1",
            f"[Etherscan v2 API] {result['result'] if result['result'] is not None else result['message']}",
        )

        return result["result"]

    def configure_timeout(self, timeout: int):
        self.timeout = timeout

    @staticmethod
    def is_valid_api_key(api_key: str) -> bool:
        return bool(re.match(r"^[A-Z0-9]{34}$", api_key))

    @staticmethod
    def is_supported_chain(chain_id: int, api_key: str) -> bool:
        url = f"{Etherscan.endpoint}/?chainid={chain_id}&apiKey={api_key}"

        response = httpx.get(url)
        response.raise_for_status()

        return response.json()["result"] != "Missing or unsupported chainid parameter"

    @staticmethod
    def chainlist() -> dict:
        response = httpx.get(f"{Etherscan.endpoint}/chainlist")

        response.raise_for_status()
        return response.json()
