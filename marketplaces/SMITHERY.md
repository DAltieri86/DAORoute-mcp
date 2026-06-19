# Smithery Publishing Notes

Smithery can publish hosted MCP servers by URL.

## Listing Copy

Name:

```text
DaoRoute
```

Short description:

```text
Non-custodial MCP decision layer for AI agents evaluating stablecoin allocation routes with risk scoring, security gates, evidence snapshots, execution metadata, and signed attestations.
```

Tags:

```text
mcp, defi, ai-agents, stablecoins, risk-scoring, security-gates, non-custodial, attestations, evidence
```

## Publish URL

Use the stable DaoRoute MCP endpoint:

```text
https://YOUR_DAOROUTE_ENDPOINT/mcp
```

## Config Schema

Use this schema for API key configuration:

```json
{
  "type": "object",
  "properties": {
    "apiKey": {
      "type": "string",
      "title": "DaoRoute API Key",
      "description": "Pilot API key issued by DaoRoute.",
      "x-from": "user"
    }
  },
  "required": ["apiKey"]
}
```

## CLI Shape

Example shape:

```bash
smithery mcp publish "https://YOUR_DAOROUTE_ENDPOINT/mcp" \
  -n @daoroute/daoroute \
  --config-schema '{"type":"object","properties":{"apiKey":{"type":"string","title":"DaoRoute API Key","description":"Pilot API key issued by DaoRoute.","x-from":"user"}},"required":["apiKey"]}'
```

## Scanner Access

If Smithery cannot scan because authentication is required:

1. provide a temporary pilot scanner key;
2. configure the server to return an auth-aware error instead of hiding the
   tool surface entirely;
3. alternatively provide manual metadata using the server-card shape included
   in `.well-known/mcp/server-card.json`.

## Boundaries

Smithery copy must preserve the pilot framing:

- free controlled pilot;
- API key required;
- non-custodial;
- no guaranteed returns;
- no investment advice;
- no transaction signing or broadcasting by DaoRoute.
