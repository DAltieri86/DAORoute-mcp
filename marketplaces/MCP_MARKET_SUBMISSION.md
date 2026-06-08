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

Category:

```text
DeFi / Finance / Data / Agent Tools
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
https://daltieri86.github.io/DAORoute-landing/
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

1. Smithery URL listing.
2. MCP Find / MCP Directory style directories.
3. Official MCP Registry after endpoint and metadata are stable.
4. GitHub topic discovery.
5. Community posts after the listing URL is live.

## Important Marketplace Notes

The official MCP Registry supports remote servers with a `remotes` field in
`server.json`, including Streamable HTTP transport and configurable headers.
Smithery supports URL publishing for Streamable HTTP servers and can scan tool
metadata; if auth blocks scanning, publish a static server card or provide a
scanner API key.

Avoid promising APY, automated trading, or investment advice in marketplace
copy.
