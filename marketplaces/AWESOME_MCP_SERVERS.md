# awesome-mcp-servers PR Asset

Use this asset when opening a pull request to an `awesome-mcp-servers` style
repository.

## Suggested Category

```text
Finance / DeFi
```

If that category does not exist, use:

```text
Data / Analytics
```

## Exact README Entry

```markdown
- [DaoRoute](https://github.com/DAltieri86/DAORoute-mcp) - Non-custodial Streamable HTTP MCP decision layer for AI agents evaluating stablecoin allocation routes with risk scoring, security gates, evidence snapshots, execution metadata, and signed attestations. Free controlled pilot; API key required.
```

## PR Title

```text
Add DaoRoute MCP server
```

## PR Body

```markdown
Adds DaoRoute, a non-custodial Streamable HTTP MCP server for AI agents and DeFi automation builders evaluating stablecoin allocation routes.

DaoRoute exposes four read-only tools:

- `get_market_snapshot`
- `get_pool_evidence`
- `get_protocol_security_status`
- `get_optimal_allocation`

The public repository contains pilot docs, integration examples, marketplace metadata, redacted sample requests/responses, and API key policy. The private decision engine, model weights, raw data, secrets, and production infrastructure are not included.

Product boundary: DaoRoute does not custody funds, sign transactions, broadcast transactions, guarantee returns, or provide investment advice.

Landing: https://www.daoroute.com/
```

## Notes

- Do not include a pilot API key in the PR.
- Do not include a temporary ngrok endpoint.
- If the list requires a live endpoint, use `https://YOUR_STABLE_DAOROUTE_MCP_ENDPOINT/mcp` only after the endpoint is stable.
