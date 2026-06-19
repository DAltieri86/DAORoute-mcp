# DaoRoute Marketplace Listing Assets

This folder contains public listing material for MCP directories, registries,
and reviewers.

DaoRoute is in a **free controlled pilot**. The files here are intentionally
limited to public copy, metadata, tool names, integration boundaries, and
directory-specific submission text.

They do not contain:

- pilot API keys;
- private endpoints;
- model weights;
- raw datasets;
- scoring internals;
- production infrastructure;
- wallet secrets;
- pricing or billing material.

## Canonical Public Details

```text
Name: DaoRoute
Landing: https://www.daoroute.com/
Repository: https://github.com/DAltieri86/DAORoute-mcp
Pilot contact: softwaretamrsv@gmail.com
Transport: Streamable HTTP
Authentication: API key required during the free controlled pilot
Endpoint placeholder: https://YOUR_STABLE_DAOROUTE_MCP_ENDPOINT/mcp
```

Use a stable MCP endpoint in directory listings only after it is ready. Do not
publish temporary tunnels or scanner credentials in public fields.

## Public Positioning

Short description:

```text
Non-custodial MCP decision layer for AI agents evaluating stablecoin allocation routes with risk scoring, security gates, evidence snapshots, execution metadata, and signed attestations.
```

Long description:

```text
DaoRoute is a free controlled-pilot MCP server for AI agents and DeFi automation builders evaluating stablecoin allocation routes. It returns structured, non-custodial decision evidence: market snapshots, one-pool evidence, live protocol security status, allocation context, execution metadata, and optional short-lived Ed25519 attestations.

DaoRoute is designed as a decision layer, not a wallet or trading bot. It does not custody funds, sign transactions, broadcast transactions, guarantee returns, provide investment advice, expose raw databases, or distribute private model internals.
```

Tags:

```text
mcp, defi, ai-agents, stablecoins, risk-scoring, security-gates, non-custodial, attestations, evidence
```

## Tool Surface

DaoRoute exposes exactly four read-only MCP tools:

```text
get_market_snapshot
get_pool_evidence
get_protocol_security_status
get_optimal_allocation
```

All tools support:

```json
{
  "verbosity": "compact"
}
```

Static tool metadata is available in:

```text
.well-known/mcp/server-card.json
```

The server card declares the four tools as read-only, idempotent, and
non-destructive.

## Files

| File | Purpose |
| --- | --- |
| `GLAMA.md` | Glama listing copy. |
| `PULSEMCP.md` | PulseMCP listing copy. |
| `OFFICIAL_REGISTRY.md` | Official MCP Registry metadata notes. |
| `SMITHERY.md` | Smithery listing/config notes. |
| `AWESOME_MCP_SERVERS.md` | Awesome-list PR copy. |
| `MCP_MARKET_SUBMISSION.md` | General directory submission copy. |

## Public Boundaries

Marketplace copy must preserve these boundaries:

- free controlled pilot;
- API key required after manual review;
- non-custodial;
- no transaction signing or broadcasting by DaoRoute;
- no guaranteed returns;
- no investment advice;
- no raw database dumps;
- no private model internals.

Validate this public pack before submission:

```bash
python3 scripts/validate_public_assets.py
```
