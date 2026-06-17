# Response Guide

DaoRoute responses are designed for agents first and humans second: explicit
action, structured evidence, validation context, risk context, execution
metadata, and attestation.

## Verbosity

All tools accept `verbosity`.

```json
{
  "verbosity": "compact"
}
```

Use `compact` for normal agent loops. It preserves the directive, key metrics,
evidence summary, execution metadata, and signed attestation while removing long
diagnostic sections.

Use `full` for audit, troubleshooting, or pilot review. `full` is the default.

## Tool Roles

Use the tools in this order during pilot evaluation:

1. `get_market_snapshot`: understand current market coverage, data depth, and
   candidate pool universe.
2. `get_pool_evidence`: inspect one candidate pool before asking for portfolio
   sizing.
3. `get_protocol_security_status`: check live security status before exposure.
4. `get_optimal_allocation`: request the final portfolio-level decision packet.

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

`evidence_summary` in compact mode, or `data_snapshot` / `data_product` in full
mode, summarizes the data coverage used to shape the response.

Typical fields:

- screened pool count;
- APY history rows indexed;
- governance proposals indexed;
- governance votes indexed;
- data age;
- evidence grade;
- whether raw database export is available.

DaoRoute returns aggregate decision evidence, not raw database dumps.

## Validation Evidence

`validation_evidence` explains how mature the current evidence package is. It
is deliberately separate from the allocation directive.

Typical fields:

- `status`: current publication/readiness status;
- `evidence_pack`: aggregate evidence-pack status, including which validation
  steps are present, insufficient, or failed;
- `public_marketing_claims_allowed`: whether the evidence is cleared for public
  performance claims;
- `controlled_pilot_claims_allowed`: whether it is suitable for controlled pilot
  discussion;
- `blockers` and `warnings`: why the product is still bounded, if applicable;
- `yield_backtest`: out-of-sample yield validation against naive baselines;
- `yield_candidate`: paper-validation status for research/shadow-mode models;
- `forecast_experiment`: offline model comparison summary.

Interpretation rule:

```text
If public_marketing_claims_allowed=false, use the output for pilot evaluation
and internal policy checks only. Do not present it as a public performance track
record.
```

This field exists to make the product more transparent, not to promise returns.

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
