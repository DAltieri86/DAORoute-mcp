# API Key Policy

DaoRoute pilot access is manually reviewed.

## Why API Keys Are Required

DaoRoute is a hosted decision engine with proprietary data processing,
security gates, scoring logic, and signed responses. API keys allow the pilot to
remain controlled while the public interface is tested.

API keys provide:

- access control;
- usage attribution;
- abuse prevention;
- pilot feedback segmentation;
- a commercial boundary between the public adapter and private engine.

## Requesting Access

Email:

```text
softwaretamrsv@gmail.com
```

Include:

- name;
- project or company;
- agent stack or MCP client;
- intended DeFi workflow;
- expected testing timeline;
- whether you need a stable public endpoint for marketplace testing.

## Key Handling

Do:

- store the key in your client secret store;
- send it as `x-api-key` or `Authorization: Bearer ...`;
- rotate it if it is exposed;
- request a separate key per integration environment.

Do not:

- commit the key to GitHub;
- paste it into public issues;
- share it in screenshots;
- reuse it across unrelated clients;
- embed it in a public frontend.

## Revocation

Pilot keys may be revoked for:

- leaked credentials;
- abusive traffic;
- attempts to scrape or reverse engineer the service;
- requests outside the agreed pilot scope;
- false marketing claims using DaoRoute output.

