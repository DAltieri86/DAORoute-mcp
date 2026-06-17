# Pilot Onboarding

This guide is for approved DaoRoute pilot users.

DaoRoute is a hosted Streamable HTTP MCP server. You connect your MCP client to
the endpoint issued during onboarding. You do not run the private engine
locally.

## 1. What You Receive

Approved pilot users receive:

- hosted MCP endpoint URL;
- pilot API key;
- allowed usage scope;
- example requests and redacted responses;
- response interpretation notes;
- feedback template.

You do not receive:

- private engine source code;
- model weights;
- database dumps;
- ingestion credentials;
- wallet access;
- custody, signing, or transaction broadcasting components.

## 2. Recommended First Session

The first useful session should take 15-30 minutes.

Use this order:

1. `get_market_snapshot`
2. `get_pool_evidence`
3. `get_protocol_security_status`
4. `get_optimal_allocation`

Why this order:

- market snapshot explains the current candidate universe;
- pool evidence lets you inspect one candidate before portfolio sizing;
- security status checks live do-not-enter context;
- optimal allocation produces the final decision packet.

## 3. Configure Authentication

DaoRoute accepts a pilot key through:

```text
x-api-key: YOUR_PILOT_API_KEY
Authorization: Bearer YOUR_PILOT_API_KEY
MCP _meta.api_key
```

Use `x-api-key` unless your MCP client has a stronger native convention.

Never put the key in:

- public GitHub repos;
- browser frontends;
- screenshots;
- public issue comments;
- shared prompts.

## 4. Generic MCP Client Configuration

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

Some clients use different configuration fields. The important parts are:

- Streamable HTTP transport;
- endpoint ending in `/mcp`;
- API key sent on every request.

## 5. First Tool Call: Market Snapshot

```json
{
  "tool": "get_market_snapshot",
  "arguments": {
    "asset": "USDC",
    "chain": "auto",
    "risk_profile": "conservative",
    "min_pool_tvl_usd": 20000000,
    "stablecoin_only": false,
    "max_pools": 10
  }
}
```

Use this to understand:

- indexed pool universe;
- protocol and chain coverage;
- evidence depth;
- candidate pools;
- suggested next actions.

This tool does not expose raw database dumps.

## 6. Second Tool Call: Pool Evidence

```json
{
  "tool": "get_pool_evidence",
  "arguments": {
    "protocol": "aave",
    "chain": "ethereum",
    "token_symbol": "USDC",
    "history_days": 365
  }
}
```

Use this to inspect:

- pool metadata;
- APR/APY history statistics;
- TVL context;
- risk fields;
- evidence grade;
- data quality signals.

## 7. Third Tool Call: Security Status

```json
{
  "tool": "get_protocol_security_status",
  "arguments": {
    "protocol": "aave"
  }
}
```

If the result is `watch` or `compromised`, safety should override yield or
allocation interest.

Also inspect `security_cache_state`, `security_status_source`,
`last_checked_at`, and `data_age_seconds`. A fresh `clear` status is stronger
than a missing-cache `clear` status.

## 8. Fourth Tool Call: Allocation Candidate

Start with simulated capital:

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
    "attestation_required": true
  }
}
```

Important:

- `signer_address` is used for metadata and route planning.
- DaoRoute does not sign with that address.
- DaoRoute does not broadcast transactions.
- The client remains responsible for review, policy checks, signing,
  execution, and monitoring.

## 9. What Good Output Looks Like

A useful response should make these fields easy to consume:

- `recommended_action`;
- `security_status`;
- `evidence_snapshot`;
- `portfolio_expected_apy_net_of_fee`;
- `allocations`;
- `execution`;
- `attestation`;
- `summary`.

Treat the response as a structured decision packet, not a guarantee.

## 10. What To Report Back

After your first test, please send:

- MCP client or framework used;
- whether configuration was clear;
- which tool was most useful;
- which response fields were confusing;
- whether the output was agent-actionable;
- fields you expected but did not receive;
- whether you would use DaoRoute before real allocation review;
- whether API-key pricing, route fee, or both would fit your workflow.

Use [`PILOT_FEEDBACK.md`](PILOT_FEEDBACK.md) if you want a structured template.
