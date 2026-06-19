# DaoRoute Integrations

DaoRoute is a hosted Streamable HTTP MCP server. These guides help approved
pilot users connect common agent stacks in a few minutes without running the
private engine locally.

Canonical public entry point:

```text
https://www.daoroute.com/
```

Pilot access:

```text
softwaretamrsv@gmail.com
```

## Available Tools

DaoRoute exposes exactly four MCP tools during the free controlled pilot:

| Tool | Use first when |
| --- | --- |
| `get_market_snapshot` | You need current market coverage, candidate pools, data depth, and suggested next actions. |
| `get_pool_evidence` | You want detailed read-only evidence for one protocol/chain/token candidate. |
| `get_protocol_security_status` | You need live security state and safety override context for a protocol. |
| `get_optimal_allocation` | You need the final non-custodial allocation decision packet. |

All tools accept:

```json
{
  "verbosity": "compact"
}
```

Use `compact` for normal agent loops and marketplace demos. Use `full` for
pilot review and deeper diagnostics. For allocation responses, compact mode
keeps the directive, evidence summary, execution metadata, fee fields, and
attestation.

## Guides

- [Claude Desktop / Cursor](claude-desktop-cursor.md)
- [LangChain / LangGraph](langchain-langgraph.md)
- [OpenAI Agents SDK](openai-agents-sdk.md)
- [ElizaOS](elizaos.md)
- [Generic remote MCP](generic-remote-mcp.md)

## Common Boundaries

DaoRoute does not custody funds, sign transactions, broadcast transactions,
guarantee returns, or provide investment advice. Treat responses as structured
decision packets for policy review, simulation, and user approval.

Read response semantics in [`../docs/RESPONSE_GUIDE.md`](../docs/RESPONSE_GUIDE.md)
and product boundaries in
[`../docs/SECURITY_AND_BOUNDARIES.md`](../docs/SECURITY_AND_BOUNDARIES.md).
