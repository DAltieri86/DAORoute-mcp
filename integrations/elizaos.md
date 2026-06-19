# ElizaOS Integration

Use this guide when you want an ElizaOS agent or plugin action to query
DaoRoute over remote MCP.

## Prerequisites

- Approved DaoRoute pilot access.
- Hosted MCP endpoint issued during onboarding, ending in `/mcp`.
- Pilot API key stored as an environment variable.
- Node project with the official MCP TypeScript SDK available.

Request access at:

```text
softwaretamrsv@gmail.com
```

## Environment

```bash
export DAOROUTE_MCP_URL="https://YOUR_DAOROUTE_ENDPOINT/mcp"
export DAOROUTE_PILOT_API_KEY="YOUR_PILOT_API_KEY"
```

## MCP Client Helper

Create a helper inside your ElizaOS plugin or action package:

```ts
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

export async function callDaoRouteMarketSnapshot() {
  const url = process.env.DAOROUTE_MCP_URL;
  const apiKey = process.env.DAOROUTE_PILOT_API_KEY;

  if (!url || !apiKey) {
    throw new Error("DAOROUTE_MCP_URL and DAOROUTE_PILOT_API_KEY are required");
  }

  const client = new Client({
    name: "elizaos-daoroute-client",
    version: "0.1.0"
  });

  const transport = new StreamableHTTPClientTransport(
    new URL(url),
    {
      requestInit: {
        headers: {
          "x-api-key": apiKey
        }
      }
    }
  );

  await client.connect(transport);

  try {
    return await client.callTool({
      name: "get_market_snapshot",
      arguments: {
        asset: "USDC",
        chain: "auto",
        risk_profile: "conservative",
        min_pool_tvl_usd: 20000000,
        stablecoin_only: false,
        max_pools: 10,
        verbosity: "compact"
      }
    });
  } finally {
    await client.close();
  }
}
```

## Action Pattern

Wrap the helper in an ElizaOS action that:

1. Calls `get_market_snapshot`.
2. Extracts `market_summary.headline`, `top_pools`, `data_product`, and
   `attestation`.
3. Refuses to present the result as a return guarantee.
4. Routes any execution intent to a separate human or policy approval step.

## How To Read The Response

For the first action, read:

- `market_summary.headline`
- `market_summary.candidate_pools`
- `top_pools`
- `data_product.evidence_grade`
- `recommended_use`
- `attestation`

See [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md).

## Boundaries

DaoRoute is non-custodial. It does not manage wallets, sign transactions, or
broadcast transactions. ElizaOS agents should treat DaoRoute output as decision
evidence that still requires policy review.
