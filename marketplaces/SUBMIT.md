# DaoRoute Marketplace Submission Playbook

This playbook is the single manual checklist for submitting DaoRoute to MCP
directories during the free controlled pilot.

## Canonical Public Details

Use these values everywhere.

```text
Name: DaoRoute
Landing: https://www.daoroute.com/
Repository: https://github.com/DAltieri86/DAORoute-mcp
Pilot contact: softwaretamrsv@gmail.com
Transport: Streamable HTTP
Authentication: API key required during the free controlled pilot
Endpoint placeholder: https://YOUR_STABLE_DAOROUTE_MCP_ENDPOINT/mcp
```

Do not submit a temporary ngrok URL unless the directory explicitly supports
temporary private review. Prefer a stable endpoint such as a reserved tunnel or
`mcp.daoroute.com` once configured.

## Canonical Description

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

## Tools

DaoRoute exposes exactly four read-only MCP tools:

```text
get_market_snapshot
get_pool_evidence
get_protocol_security_status
get_optimal_allocation
```

All tools accept:

```json
{
  "verbosity": "compact"
}
```

Tool annotations are declared in `.well-known/mcp/server-card.json`:

```json
{
  "readOnlyHint": true,
  "idempotentHint": true,
  "destructiveHint": false
}
```

`server.example.json` is reserved for official MCP Registry server metadata and
does not duplicate tool schemas because the registry schema does not define a
top-level `tools` field.

## Pre-Submission Checklist

- [ ] Landing page is live at `https://www.daoroute.com/`.
- [ ] Public repo is pushed and clean.
- [ ] No secrets, API keys, temporary tunnel tokens, model files, or database dumps are present.
- [ ] Stable MCP endpoint is chosen.
- [ ] A dedicated scanner pilot key is created if a directory needs to call the server.
- [ ] Scanner key is never pasted into public repo, PR body, screenshots, or listing copy.
- [ ] `python3 scripts/validate_public_assets.py` passes locally.
- [ ] Marketplace copy does not promise APY, returns, automated trading, or investment advice.

## 1. Glama

Asset file:

```text
marketplaces/GLAMA.md
```

Manual steps:

1. Open Glama submission flow.
2. Use the canonical name, short description, long description, tags, and URLs.
3. Use the stable MCP endpoint only when available.
4. If Glama requires scanning, provide a dedicated pilot scanner key through
   the directory's private credential field only.
5. Confirm the listing states `API key required during the free controlled pilot`.

Checklist:

- [ ] Glama listing created or draft saved.
- [ ] No temporary endpoint published.
- [ ] No key exposed in public fields.

## 2. PulseMCP

Asset file:

```text
marketplaces/PULSEMCP.md
```

Manual steps:

1. Open PulseMCP submission flow.
2. Paste the one-liner, description, tags, tool list, and links.
3. Use the stable endpoint placeholder until the endpoint is final.
4. Mark the server as remote Streamable HTTP and API-key gated.

Checklist:

- [ ] PulseMCP listing created or draft saved.
- [ ] Tool list contains exactly four tools.
- [ ] Description preserves non-custodial/no-guarantee boundaries.

## 3. Official MCP Registry

Asset files:

```text
server.example.json
marketplaces/OFFICIAL_REGISTRY.md
```

Manual steps:

1. Copy `server.example.json` to `server.json` outside this repo or in a release
   branch when ready.
2. If required, replace `https://{pilot_host}/mcp` with the stable MCP endpoint.
3. Keep the `x-api-key` header marked as `isSecret: true`.
4. Keep `websiteUrl` as `https://www.daoroute.com/`.
5. Submit according to registry instructions.

Checklist:

- [ ] `server.json` validates as JSON.
- [ ] Header secret marker is present.
- [ ] No tool schemas were forced into `server.json`.
- [ ] Stable endpoint is used only when confirmed.

## 4. Smithery

Asset file:

```text
marketplaces/SMITHERY.md
```

Manual steps:

1. Use the stable MCP endpoint.
2. Configure API-key input as a user-provided secret.
3. If Smithery cannot scan an authenticated server, provide either:
   - a dedicated scanner pilot key through private configuration; or
   - static tool metadata from `.well-known/mcp/server-card.json`.
4. Keep the listing copy aligned with the canonical description.

Checklist:

- [ ] Smithery listing created or draft saved.
- [ ] API key stored only in Smithery secret/config field.
- [ ] Tool metadata shows read-only/idempotent/non-destructive annotations.

## 5. awesome-mcp-servers

Asset file:

```text
marketplaces/AWESOME_MCP_SERVERS.md
```

Manual steps:

1. Fork the target awesome list.
2. Add the exact README entry under Finance/DeFi or Data/Analytics.
3. Open a PR with the prepared title and PR body.
4. Do not include an endpoint unless the repository requires one and the
   endpoint is stable.

Checklist:

- [ ] Fork created.
- [ ] README entry added.
- [ ] PR opened.
- [ ] PR body preserves non-custodial/no-guarantee boundaries.

## After Submission

Track:

- directory URL;
- submission date;
- status;
- reviewer feedback;
- whether a scanner key was issued;
- whether any key must be revoked after review.

Do not publish performance claims while `controlled_pilot_only` remains the
current posture.
