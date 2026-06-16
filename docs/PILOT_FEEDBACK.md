# Pilot Feedback Template

Please use this template after your first DaoRoute pilot session.

## 1. Basic Context

```text
Name:
Project/company:
MCP client or agent framework:
Primary use case:
Date tested:
```

## 2. Setup

```text
Was the endpoint easy to configure? yes/no
Was API key handling clear? yes/no
Which auth method did you use? x-api-key / Authorization Bearer / _meta.api_key
Any connection or transport issues?
```

## 3. Tool Flow

Recommended flow:

1. `get_market_snapshot`
2. `get_pool_evidence`
3. `get_protocol_security_status`
4. `get_optimal_allocation`

```text
Did this order make sense for your agent? yes/no
Which tool was most useful?
Which tool was least clear?
Did any tool return too much or too little information?
```

## 4. Response Quality

```text
Was the recommended_action clear?
Was the security_status useful?
Was the market/pool evidence useful?
Was the allocation output easy for an agent to parse?
Was the execution metadata useful in your workflow?
Was the attestation useful or unnecessary?
```

## 5. Missing Fields

```text
What fields would make the response more useful?
What risk data did you expect but not see?
What execution metadata did you expect but not see?
What format would be easier for your client?
```

## 6. Product Fit

```text
Would you use DaoRoute before a real DeFi allocation review? yes/no/maybe
Would API-key pricing fit your workflow? yes/no/maybe
Would route/referrer fee pricing fit your workflow? yes/no/maybe
What would need to change before you would pay?
```

## 7. Safety Boundaries

```text
Was it clear that DaoRoute is non-custodial? yes/no
Was it clear that DaoRoute does not guarantee returns? yes/no
Was it clear that DaoRoute does not sign or broadcast transactions? yes/no
```

## 8. Final Notes

```text
What should DaoRoute improve next?
Would you be open to a follow-up call?
Can we quote any part of your feedback publicly? yes/no
```

