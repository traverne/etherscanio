# etherscanio: Lightweight Python wrapper for the Etherscan v2 Multi-chain API

[![PyPI - Version](https://img.shields.io/pypi/v/etherscanio.svg)](https://pypi.org/project/etherscanio)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/etherscanio.svg)](https://pypi.org/project/etherscanio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, clean, and intuitive Python client for interacting with Etherscan's API across multiple blockchain networks.

## Features

- **Simple & Intuitive** - Clean, Pythonic interface
- **Multi-chain Support** - Works with Ethereum, BSC, Polygon, and more
- **Minimal Dependencies** - Only requires httpx
- **Modular Design** - Organized API endpoints into logical modules

## Installation

```bash
pip install etherscanio
```

## Quick Start

```python
from etherscan import Etherscan

# Initialize with your API key
client = Etherscan(chain_id=1, api_key="YOUR_API_KEY")

# Or use environment variable ETHERSCAN_API_KEY
client = Etherscan(chain_id=1)

# Get account balance
balance = client.accounts.get_balance("0x...")

# Get transaction details
tx = client.transactions.get_transaction("0x...")

# Get gas prices
gas = client.gastracker.get_gas_oracle()
```

## Supported Chains

The library supports all chains available in the Etherscan v2 API. Use the appropriate chain ID for your target network. For a complete list of supported chains and their IDs, visit the [official documentation](https://docs.etherscan.io/supported-chains).

You can also fetch the list programmatically:

```python
chains = Etherscan.chainlist()
```

## API Modules

The API is organized into logical modules for easy access to different Etherscan endpoints.

### Accounts

Access account-related data including balances, transaction history, and token holdings.

```python
# Get ETH balance for an address
balance = client.accounts.get_balance("0x...")

# Get ERC20 token balance
token_balance = client.accounts.get_token_balance(
    address="0x...",
    contract_address="0x..."
)

# Get transaction history for an address
txs = client.accounts.get_transactions("0x...")
```

### Transactions

Query transaction details, receipts, and execution status.

```python
# Get transaction receipt
receipt = client.transactions.get_transaction_receipt("0x...")

# Check transaction status
status = client.transactions.get_transaction_status("0x...")
```

### Tokens

Retrieve information about ERC20 and ERC721 tokens including supply, holders, and transfers.

```python
# Get total supply of an ERC20 token
supply = client.tokens.get_token_supply("0x...")

# Get token information
info = client.tokens.get_token_info("0x...")
```

### Blocks

Access block data including rewards, timestamps, and block production information.

```python
# Get block reward information
reward = client.blocks.get_block_reward(12345678)

# Get estimated time until a future block
countdown = client.blocks.get_block_countdown(12345678)
```

### Gas Tracker

Monitor current gas prices and estimate transaction costs.

```python
# Get current gas price recommendations
gas = client.gastracker.get_gas_oracle()

# Estimate gas for a transaction
estimate = client.gastracker.estimate_gas(
    to="0x...",
    value=1000000000000000000,
    gas_price=20000000000
)
```

### Smart Contracts

Interact with smart contracts, retrieve source code, and verify contract deployments.

```python
# Get contract ABI
abi = client.contracts.get_contract_abi("0x...")

# Get verified source code
source = client.contracts.get_source_code("0x...")

# Verify and publish contract source code
result = client.contracts.verify_solidity_source_code(
    address="0x...",
    contract_name="MyContract",
    code_format="solidity-single-file",
    source_code="pragma solidity...",
    compiler_version="v0.8.0+commit.c7dfd78e"
)
```

### Statistics

Access network-wide statistics including supply metrics and price data.

```python
# Get total ETH supply
supply = client.statistics.get_total_supply()

# Get current ETH price in USD
price = client.statistics.get_eth_price()
```

### Proxy (Direct Ethereum JSON-RPC)

Make direct Ethereum JSON-RPC calls through Etherscan's infrastructure.

```python
# Get the latest block number
block_num = client.eth.get_block_number()

# Call a contract method (read-only)
result = client.eth.call(
    to="0x...",
    data="0x..."
)

# Get transaction count for an address (nonce)
count = client.eth.get_transaction_count("0x...")
```

## Configuration

### API Key

Set your API key in one of three ways:

1. **Pass directly:**
   ```python
   client = Etherscan(chain_id=1, api_key="YOUR_KEY")
   ```

2. **Environment variable:**
   ```bash
   export ETHERSCAN_API_KEY="YOUR_KEY"
   ```
   ```python
   client = Etherscan(chain_id=1)
   ```

3. **No key (limited requests):**
   ```python
   client = Etherscan(chain_id=1)  # Uses public rate limits
   ```

### Timeout

Configure request timeout:

```python
client = Etherscan(chain_id=1, api_key="YOUR_KEY")
client.configure_timeout(30)  # 30 seconds
```

## Error Handling

```python
from etherscan import Etherscan, EtherscanException

try:
    client = Etherscan(chain_id=999, api_key="YOUR_KEY")
except EtherscanException as e:
    print(f"Error: {e}")
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/traverne/etherscanio.git
cd etherscanio

# Install with hatch
pip install hatch

# Enter development environment
hatch shell
```

### Running Tests

```bash
# Run tests
hatch run test

# Run with coverage
hatch run test-cov
```

### Linting

```bash
# Check code
hatch run lint:check

# Format code
hatch run lint:fmt
```

## Requirements

- Python >=3.9
- httpx

## License

`etherscanio` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Links

- **Documentation**: [GitHub README](https://github.com/traverne/etherscanio#readme)
- **Source Code**: [GitHub](https://github.com/traverne/etherscanio)
- **Issue Tracker**: [GitHub Issues](https://github.com/traverne/etherscanio/issues)
- **PyPI**: [pypi.org/project/etherscanio](https://pypi.org/project/etherscanio)
- **Etherscan API Docs**: [docs.etherscan.io](https://docs.etherscan.io/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Built with [Hatch](https://hatch.pypa.io/) and powered by [httpx](https://www.python-httpx.org/).

---

Made with ❤️ by [Athen Traverne](https://github.com/traverne)
