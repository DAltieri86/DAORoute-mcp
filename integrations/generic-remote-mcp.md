# Generic Remote MCP Integration

Use this guide for any MCP-compatible client that can connect to a remote
Streamable HTTP server.

## Prerequisites

- Approved DaoRoute pilot access.
- Hosted MCP endpoint issued during onboarding, ending in `/mcp`.
- Pilot API key stored outside source control.

Request access at:

```text
softwaretamrsv@gmail.com
```

## Client Configuration

Use this configuration shape when your client accepts `mcpServers` JSON:

```json
{
  "mcpServers": {
    "daoroute": {
      "transport": "streamable-http",
      "url": "https://YOUR_DAOROUTE_ENDPOINT/mcp",
      "headers": {
        "x-api-key": "YOUR_PILOT_API_KEY"
      }
    }
  }
}
```

The same example is available as
[`../examples/client-config.generic.json`](../examples/client-config.generic.json).

DaoRoute accepts pilot API keys in any of these forms:

```text
x-api-key: YOUR_PILOT_API_KEY
Authorization: Bearer YOUR_PILOT_API_KEY
MCP _meta.api_key
```

Prefer `x-api-key` unless your client has a native bearer-token convention.

## Tool Discovery

After connecting, list tools. The expected pilot tool set is:

```text
get_market_snapshot
get_optimal_allocation
get_pool_evidence
get_protocol_security_status
```

## First Tool Call

Call `get_market_snapshot` with:

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

Use `get_market_snapshot` as a pre-flight scan:

- `market_summary` tells you the current candidate universe.
- `protocol_breakdown` and `top_pools` give coverage context.
- `data_product` explains evidence depth without exposing raw datasets.
- `recommended_use` tells the agent what this response is suitable for.
- `attestation` lets a client verify the response payload.

See [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md).

## Boundaries

DaoRoute does not custody funds, sign transactions, broadcast transactions, or
guarantee returns. Clients remain responsible for policy checks, wallet
authorization, execution, and monitoring.
