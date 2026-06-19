# Claude Desktop / Cursor Integration

Use this guide when your MCP client supports remote Streamable HTTP servers
through an `mcp.json` style configuration.

## Prerequisites

- Approved DaoRoute pilot access.
- Hosted MCP endpoint issued during onboarding, ending in `/mcp`.
- Pilot API key issued by DaoRoute. Do not commit it to a repository.

Request access at:

```text
softwaretamrsv@gmail.com
```

## Configuration

Add DaoRoute to your client MCP configuration:

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

Some clients name the transport field `type` instead of `transport`. If your
client rejects the config above, keep the same URL and headers and use:

```json
{
  "type": "streamable-http"
}
```

## First Tool Call

Ask your client to call `get_market_snapshot` with:

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

Start with:

- `market_summary.headline`
- `protocol_breakdown`
- `top_pools`
- `data_product`
- `recommended_use`
- `attestation`

See [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md) for field-level
interpretation.

## Boundaries

DaoRoute is non-custodial. It does not sign or broadcast transactions and does
not guarantee returns. If later calls return `watch` or `compromised` security
status, security should override yield or allocation interest.
