# OpenAI Agents SDK Integration

Use this guide when you want an OpenAI Agents SDK agent to consume DaoRoute as a
remote Streamable HTTP MCP server.

## Prerequisites

- Approved DaoRoute pilot access.
- Hosted MCP endpoint issued during onboarding, ending in `/mcp`.
- Pilot API key stored in your environment or secret manager.
- Python environment with the OpenAI Agents SDK installed.

Request access at:

```text
softwaretamrsv@gmail.com
```

## Environment

```bash
export DAOROUTE_MCP_URL="https://YOUR_DAOROUTE_ENDPOINT/mcp"
export DAOROUTE_PILOT_API_KEY="YOUR_PILOT_API_KEY"
```

## Streamable HTTP MCP Server Registration

```python
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp
from agents.model_settings import ModelSettings


async def main() -> None:
    async with MCPServerStreamableHttp(
        name="DaoRoute",
        params={
            "url": os.environ["DAOROUTE_MCP_URL"],
            "headers": {
                "x-api-key": os.environ["DAOROUTE_PILOT_API_KEY"],
            },
            "timeout": 30,
        },
        cache_tools_list=True,
        max_retry_attempts=2,
    ) as daoroute:
        agent = Agent(
            name="DaoRoute pilot agent",
            instructions=(
                "Use DaoRoute only for non-custodial DeFi decision evidence. "
                "Never claim guaranteed returns. Never imply that DaoRoute signs "
                "or broadcasts transactions."
            ),
            mcp_servers=[daoroute],
            model_settings=ModelSettings(tool_choice="required"),
        )

        result = await Runner.run(
            agent,
            "Call get_market_snapshot with asset USDC, chain auto, "
            "risk_profile conservative, min_pool_tvl_usd 20000000, "
            "stablecoin_only false, max_pools 10, verbosity compact. "
            "Summarize the market_summary headline, top pool count, "
            "data_product evidence grade, and attestation status.",
        )
        print(result.final_output)


asyncio.run(main())
```

## First Tool Call Arguments

The agent should call `get_market_snapshot` with:

```json
{
  "asset": "USDC",
  "chain": "auto",
  "risk_profile": "conservative",
  "min_pool_tvl_usd": 20000000,
  "stablecoin_only": false,
  "max_pools": 10,
  "verbosity": "compact"
}
```

## How To Read The Response

Ask the agent to preserve these fields in its reasoning trace or final summary:

- `market_summary`
- `protocol_breakdown`
- `top_pools`
- `data_product`
- `recommended_use`
- `attestation.valid_until`

See [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md) for response
semantics.

## Boundaries

DaoRoute output is informational and experimental during the free controlled
pilot. Your agent should not auto-sign or auto-broadcast from a DaoRoute
response. Add human or policy approval before execution.
