# MCP Marketplace Submission Guide

Use this guide when submitting DaoRoute to MCP directories and marketplaces.

## Recommended Listing Copy

Name:

```text
DaoRoute
```

Short description:

```text
Non-custodial MCP decision layer for AI agents evaluating stablecoin allocation routes with risk scoring, security gates, evidence snapshots, execution metadata, and signed attestations.
```

Long description:

```text
DaoRoute is a free controlled-pilot MCP server for AI agents and DeFi automation builders evaluating stablecoin allocation routes. It returns structured, non-custodial decision evidence: market snapshots, one-pool evidence, live protocol security status, allocation context, execution metadata, and optional short-lived Ed25519 attestations.

DaoRoute is designed as a decision layer, not a wallet or trading bot. It does not custody funds, sign transactions, broadcast transactions, guarantee returns, provide investment advice, expose raw databases, or distribute private model internals.
```

Category:

```text
DeFi / Finance / Data / Agent Tools
```

Tags:

```text
mcp, defi, ai-agents, stablecoins, risk-scoring, security-gates, non-custodial, attestations, evidence
```

Capabilities:

```text
Remote Streamable HTTP MCP server; API-key gated free controlled pilot; read-only tools; market coverage snapshots; pool evidence; protocol security status; stablecoin allocation decision packets; execution metadata; signed attestations.
```

Transport:

```text
Streamable HTTP
```

Authentication:

```text
API key required during controlled pilot
```

Tools:

```text
get_market_snapshot
get_pool_evidence
get_optimal_allocation
get_protocol_security_status
```

Public repo:

```text
https://github.com/DAltieri86/DAORoute-mcp
```

Landing:

```text
https://www.daoroute.com/
```

Contact:

```text
softwaretamrsv@gmail.com
```

## Required Before Submission

- stable HTTPS MCP endpoint;
- pilot API key for marketplace scanner if required;
- public repository pushed to GitHub;
- `server.json` prepared from `server.example.json`;
- no secrets in repository;
- no backend/private engine code in repository;
- landing page live;
- sample response available.

## Suggested Submission Order

1. Glama.
2. PulseMCP.
3. Official MCP Registry after endpoint and metadata are stable.
4. Smithery URL listing.
5. awesome-mcp-servers PR.
6. GitHub topic discovery.
7. Community posts after the listing URL is live.

## Important Marketplace Notes

The official MCP Registry supports remote servers with a `remotes` field in
`server.json`, including Streamable HTTP transport and configurable headers.
Smithery supports URL publishing for Streamable HTTP servers and can scan tool
metadata; if auth blocks scanning, publish a static server card or provide a
scanner API key.

Avoid promising APY, automated trading, or investment advice in marketplace
copy.
