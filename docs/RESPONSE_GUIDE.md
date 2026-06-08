# Response Guide

DaoRoute responses are designed for agents first and humans second: explicit
action, structured evidence, risk context, execution metadata, and attestation.

## Recommended Action

Allowed values:

```text
PROCEED
REDUCE_EXPOSURE
AVOID
EXIT_IMMEDIATELY
```

Security overrides always take priority over yield or allocation signals.

## Evidence Snapshot

`evidence_snapshot` summarizes the data coverage used to shape the response.

Typical fields:

- screened pool count;
- APY history rows indexed;
- governance proposals indexed;
- governance votes indexed;
- data age;
- evidence grade;
- whether raw database export is available.

DaoRoute returns aggregate decision evidence, not raw database dumps.

## Execution Metadata

Execution fields are non-custodial.

`calldata_available=true` means the response may include metadata required by a
client-side execution adapter. It does not mean DaoRoute has signed or sent a
transaction.

The client remains responsible for:

- policy checks;
- wallet authorization;
- signing;
- broadcasting;
- slippage validation;
- monitoring.

## Attestation

Attestations are short-lived signatures over the response payload.

Use them to verify what the engine returned at a specific timestamp. Do not use
expired attestations for execution.

