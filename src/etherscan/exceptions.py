class EtherscanError(Exception):
    pass


def validate(condition: bool, message: str) -> None:
    if not condition:
        raise EtherscanError(message)
