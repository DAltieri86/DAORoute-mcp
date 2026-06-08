# Security And Product Boundaries

DaoRoute is non-custodial by design.

## DaoRoute Does

- provide structured MCP responses;
- score and rank candidate allocation routes;
- expose security status;
- return aggregate evidence snapshots;
- provide unsigned execution metadata;
- sign response payloads when attestation is enabled.

## DaoRoute Does Not

- custody funds;
- manage wallets;
- sign transactions;
- broadcast transactions;
- guarantee APY;
- guarantee capital preservation;
- provide investment advice;
- expose raw private datasets;
- distribute model internals.

## Security Precedence

If a protocol status is `compromised`, the safe action is
`EXIT_IMMEDIATELY`.

If a protocol status is `watch`, the safe action is usually
`REDUCE_EXPOSURE`.

Security state overrides cached predictive or allocation data.

## Agent Policy Recommendation

Agents integrating DaoRoute should implement their own guardrails:

- never auto-sign solely from an MCP response;
- require user or policy approval for execution;
- reject expired attestations;
- reject responses with stale data age;
- apply capital limits independently;
- log request IDs and response hashes.

