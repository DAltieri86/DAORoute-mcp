# Glama Listing Asset

Use this copy when submitting DaoRoute to Glama.

## Name

```text
DaoRoute
```

## Short Description

```text
Non-custodial MCP decision layer for AI agents evaluating stablecoin allocation routes with risk scoring, security gates, evidence snapshots, execution metadata, and signed attestations.
```

## Long Description

```text
DaoRoute is a free controlled-pilot MCP server for AI agents and DeFi automation builders evaluating stablecoin allocation routes. It returns structured, non-custodial decision evidence: market snapshots, one-pool evidence, live protocol security status, allocation context, execution metadata, and optional short-lived Ed25519 attestations.

DaoRoute is designed as a decision layer, not a wallet or trading bot. It does not custody funds, sign transactions, broadcast transactions, guarantee returns, provide investment advice, expose raw databases, or distribute private model internals.
```

## Category

```text
DeFi / Finance / Data / Agent Tools
```

## Tags

```text
mcp, defi, ai-agents, stablecoins, risk-scoring, security-gates, non-custodial, attestations, evidence
```

## Capabilities

- Remote Streamable HTTP MCP server.
- API-key gated free controlled pilot.
- Four read-only MCP tools:
  - `get_market_snapshot`
  - `get_pool_evidence`
  - `get_protocol_security_status`
  - `get_optimal_allocation`
- Compact and full response verbosity.
- Non-custodial execution metadata.
- Optional signed attestation.

## URLs

```text
Landing: https://www.daoroute.com/
Repository: https://github.com/DAltieri86/DAORoute-mcp
MCP endpoint placeholder: https://YOUR_STABLE_DAOROUTE_MCP_ENDPOINT/mcp
```

## Authentication

```text
API key required during the free controlled pilot.
```
