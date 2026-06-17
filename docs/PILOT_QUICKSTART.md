# DaoRoute Pilot Quickstart

This guide is for approved pilot users.

DaoRoute is a hosted Streamable HTTP MCP server. You do not run the private
engine locally. You connect your MCP-compatible client to the hosted endpoint
issued during pilot onboarding.

## 1. What You Receive

Approved pilot users receive:

- MCP endpoint URL;
- pilot API key;
- allowed usage scope;
- expected rate limits;
- sample requests;
- response interpretation guide;
- feedback channel.

You do not receive:

- model weights;
- raw database access;
- production `.env` files;
- private ingestion code;
- custody, signing, or transaction broadcasting components.

## 1.1 Response Verbosity

Each tool supports:

```json
{
  "verbosity": "compact"
}
```

Use `compact` for normal agent workflows and marketplace testing. It keeps the
directive, evidence summary, execution metadata, and attestation while omitting
long diagnostic blocks.

Use `full` when you want deeper audit context. `full` is the default if the
field is omitted.

## 2. Authentication

DaoRoute accepts the pilot API key through one of:

```text
x-api-key: YOUR_PILOT_API_KEY
Authorization: Bearer YOUR_PILOT_API_KEY
MCP _meta.api_key
```

Prefer `x-api-key` unless your client has a better native convention.

## 3. Start With Market Coverage

Start by asking what DaoRoute currently sees:

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

This returns aggregate coverage, protocol and chain breakdowns, top candidate
pools, data depth, validation status, and suggested next actions. It does not
expose raw database dumps.

## 4. Inspect A Pool

Use `get_pool_evidence` when a candidate pool looks interesting:

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

This returns pool metadata, APR/APY/TVL history statistics, evidence grade, and
follow-up actions.

## 5. Check Security Status

Before entering or increasing exposure, call:

```json
{
  "tool": "get_protocol_security_status",
  "arguments": {
    "protocol": "aave",
    "verbosity": "compact"
  }
}
```

Expected high-level fields:

```json
{
  "status": "clear",
  "recommended_action": "PROCEED",
  "active_alerts": [],
  "attestation": {
    "algo": "ed25519"
  }
}
```

If `status` is `watch` or `compromised`, security takes precedence over yield
or allocation signals.

## 6. Request An Allocation Candidate

Example:

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

Important:

- `signer_address` is used for metadata and execution planning.
- DaoRoute does not sign with this address.
- DaoRoute does not broadcast transactions.
- The client must review and sign any downstream transaction.

## 7. Interpret The Response

Focus on:

- `recommended_action`;
- `security_status`;
- `risk_adjusted_score`;
- `portfolio_expected_apy_net_of_fee`;
- `evidence_summary` in compact mode, or `data_snapshot` / `data_product` in
  full mode;
- `validation_evidence`, especially `controlled_pilot_claims_allowed`,
  `public_marketing_claims_allowed`, blockers, warnings, and yield baseline
  comparisons;
- `execution.calldata_available`;
- `attestation.valid_until`.

Do not treat the response as a guarantee. Treat it as a structured decision
packet for policy review, simulation, and user approval.

## 8. Feedback To Send

Useful pilot feedback:

- which MCP client or agent framework you used;
- whether auth/configuration was clear;
- which response fields were useful;
- which fields were confusing;
- whether the output was easy for an agent to act on;
- whether you need additional risk fields;
- whether the non-custodial execution metadata fits your workflow.
