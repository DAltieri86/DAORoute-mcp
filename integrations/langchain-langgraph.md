# LangChain / LangGraph Integration

Use this guide when you want a LangChain or LangGraph agent to consume DaoRoute
as a remote MCP tool server.

## Prerequisites

- Approved DaoRoute pilot access.
- Hosted MCP endpoint issued during onboarding, ending in `/mcp`.
- Pilot API key stored in your secret manager or local environment.
- Python environment with `langchain-mcp-adapters` installed.

Request access at:

```text
softwaretamrsv@gmail.com
```

## Environment

```bash
export DAOROUTE_MCP_URL="https://YOUR_DAOROUTE_ENDPOINT/mcp"
export DAOROUTE_PILOT_API_KEY="YOUR_PILOT_API_KEY"
```

## Minimal Tool Registration

```python
import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "daoroute": {
                "transport": "streamable_http",
                "url": os.environ["DAOROUTE_MCP_URL"],
                "headers": {
                    "x-api-key": os.environ["DAOROUTE_PILOT_API_KEY"],
                },
            }
        }
    )

    tools = await client.get_tools()
    tool_names = sorted(tool.name for tool in tools)
    print(tool_names)


asyncio.run(main())
```

Expected tool names:

```text
get_market_snapshot
get_optimal_allocation
get_pool_evidence
get_protocol_security_status
```

## First Tool Call

```python
import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient


MARKET_SNAPSHOT_ARGS = {
    "asset": "USDC",
    "chain": "auto",
    "risk_profile": "conservative",
    "min_pool_tvl_usd": 20000000,
    "stablecoin_only": False,
    "max_pools": 10,
    "verbosity": "compact",
}


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "daoroute": {
                "transport": "streamable_http",
                "url": os.environ["DAOROUTE_MCP_URL"],
                "headers": {
                    "x-api-key": os.environ["DAOROUTE_PILOT_API_KEY"],
                },
            }
        }
    )

    tools = await client.get_tools()
    market_snapshot = next(
        tool for tool in tools if tool.name == "get_market_snapshot"
    )
    result = await market_snapshot.ainvoke(MARKET_SNAPSHOT_ARGS)
    print(result)


asyncio.run(main())
```

## LangGraph Usage Pattern

Use `get_market_snapshot` as the first node in a DeFi routing graph, then branch
to:

1. `get_pool_evidence` for selected candidate pools.
2. `get_protocol_security_status` before any exposure decision.
3. `get_optimal_allocation` only after your policy node approves the context.

## How To Read The Response

For `get_market_snapshot`, inspect `market_summary`, `top_pools`,
`data_product`, `recommended_use`, and `attestation`.

See [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md) for response
semantics and compact/full verbosity guidance.

## Boundaries

DaoRoute is a decision layer, not a wallet. Your graph must keep its own policy
checks, approval steps, signing, broadcasting, and monitoring.
