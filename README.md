# DaoRoute MCP Pilot

DaoRoute is a non-custodial MCP decision layer for AI agents and DeFi
automation builders evaluating stablecoin allocation routes.

This repository contains the **public pilot pack**: integration notes,
marketplace metadata templates, sample MCP requests, redacted responses, and API
key policy. The private decision engine is not included.

Landing page:

```text
https://daltieri86.github.io/DAORoute-landing/
```

Pilot access:

```text
softwaretamrsv@gmail.com
```

## What DaoRoute Does

DaoRoute packages decision evidence for agent workflows:

- risk-adjusted stablecoin allocation candidates;
- live protocol security status;
- multi-source data evidence snapshots;
- fee-aware expected APY fields;
- non-custodial execution metadata;
- short-lived Ed25519 attestations.

The server currently exposes four MCP tools:

| Tool | Purpose |
| --- | --- |
| `get_optimal_allocation` | Returns an allocation decision with risk diagnostics, evidence, execution metadata, and optional attestation. |
| `get_protocol_security_status` | Returns protocol security status, recommended action, active alerts, and safety override context. |
| `get_market_snapshot` | Returns aggregate market coverage, candidate pool intelligence, protocol/chain breakdowns, and data-depth evidence. |
| `get_pool_evidence` | Returns detailed read-only evidence for one pool lookup, including APR history stats, TVL context, risk fields, and follow-up actions. |

All tools accept `verbosity: "full" | "compact"`.

- Use `compact` for agent context windows, marketplace demos, and quick
  integration tests.
- Use `full` for audit, diagnostics, and deeper pilot review.
- `full` remains the default.

## What This Repository Is Not

This is not the DaoRoute engine source code.

It does **not** include:

- private model weights;
- database dumps;
- ingestion pipelines;
- scoring internals;
- production infrastructure;
- secrets or API keys;
- custody, signing, or transaction broadcasting code.

The public surface is intentionally narrow so DaoRoute can be listed and tested
without exposing the proprietary decision engine.

## Quickstart For Pilot Users

1. Request access by emailing `softwaretamrsv@gmail.com`.
2. If approved, you receive:
   - Streamable HTTP MCP endpoint;
   - pilot API key;
   - allowed usage scope;
   - example requests;
   - response interpretation notes.
3. Configure your MCP client with the endpoint and API key.
4. Start with `get_market_snapshot` to inspect coverage and candidate pools.
5. Use `get_pool_evidence` on shortlisted pools.
6. Check `get_protocol_security_status` before considering exposure.
7. Then test `get_optimal_allocation` with a small simulated capital amount.

Generic remote MCP configuration:

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

Some clients use `Authorization: Bearer YOUR_PILOT_API_KEY` or MCP request
metadata instead of `x-api-key`. DaoRoute supports all three forms during the
pilot.

## Example Tool Call

Market snapshot:

```json
{
  "tool": "get_market_snapshot",
  "arguments": {
    "asset": "USDC",
    "chain": "auto",
    "risk_profile": "conservative",
    "min_pool_tvl_usd": 20000000,
    "stablecoin_only": false,
    "max_pools": 10,
    "verbosity": "compact"
  }
}
```

Pool evidence:

```json
{
  "tool": "get_pool_evidence",
  "arguments": {
    "protocol": "aave",
    "chain": "ethereum",
    "token_symbol": "USDC",
    "history_days": 365,
    "verbosity": "compact"
  }
}
```

Allocation decision:

```json
{
  "tool": "get_optimal_allocation",
  "arguments": {
    "capital_amount": "100000",
    "asset": "USDC",
    "chain": "auto",
    "risk_profile": "conservative",
    "signer_address": "0x1111111111111111111111111111111111111111",
    "max_slippage_bps": 100,
    "max_pools": 10,
    "max_allocation_per_pool_bps": 2000,
    "min_pools": 5,
    "time_horizon": "flexible",
    "attestation_required": true,
    "verbosity": "compact"
  }
}
```

See [`examples/`](examples/) for redacted request and response examples.

## Marketplace Readiness

This repository is prepared for MCP marketplace submission without publishing
private code.

Included:

- [`server.example.json`](server.example.json) for the official MCP Registry;
- [`marketplaces/SMITHERY.md`](marketplaces/SMITHERY.md) for Smithery listing;
- [`marketplaces/MCP_MARKET_SUBMISSION.md`](marketplaces/MCP_MARKET_SUBMISSION.md)
  for directory submission copy;
- [`docs/PILOT_ONBOARDING.md`](docs/PILOT_ONBOARDING.md) for approved-user
  onboarding;
- [`docs/PILOT_QUICKSTART.md`](docs/PILOT_QUICKSTART.md) for approved users;
- [`docs/PILOT_FEEDBACK.md`](docs/PILOT_FEEDBACK.md) for structured pilot
  feedback;
- [`docs/API_KEY_POLICY.md`](docs/API_KEY_POLICY.md) for access control;
- [`docs/SECURITY_AND_BOUNDARIES.md`](docs/SECURITY_AND_BOUNDARIES.md) for
  non-custodial limits.

## Safety And Legal Boundaries

DaoRoute:

- does not custody funds;
- does not sign transactions;
- does not broadcast transactions;
- does not guarantee returns;
- does not provide investment advice;
- does not expose raw wallet-level data;
- does not distribute private model internals.

Pilot output is informational and experimental. Clients remain responsible for
policy checks, user approval, signing, execution, monitoring, and legal review.

## License

This repository is public for review and pilot integration, but it is **not open
source software**. See [`LICENSE.md`](LICENSE.md).
