# Official MCP Registry Notes

The official MCP Registry uses `server.json` metadata.

DaoRoute should publish as a remote Streamable HTTP server after the hosted MCP
endpoint is stable.

## Preparation

1. Copy `server.example.json` to `server.json`.
2. Replace the remote URL template with the stable endpoint if marketplace
   policy requires a fixed URL.
3. Keep the `x-api-key` header marked as secret.
4. Keep `websiteUrl` set to:

   ```text
   https://www.daoroute.com/
   ```

5. Use namespace:

   ```text
   io.github.daltieri86/daoroute-mcp
   ```

6. Increment `version` for each published metadata update.

## Tool Metadata

The official registry `server.json` schema describes server/package/remote
metadata and does not define a top-level `tools` field. Do not force tool
schemas into `server.json`.

For directories that accept static tool metadata, use:

```text
.well-known/mcp/server-card.json
```

That file declares exactly four read-only tools and includes:

```json
{
  "readOnlyHint": true,
  "idempotentHint": true,
  "destructiveHint": false
}
```

## Caution

Registry metadata is public. Do not include:

- private endpoint secrets;
- temporary ngrok tokens;
- API keys;
- internal IPs;
- private model or database references.
