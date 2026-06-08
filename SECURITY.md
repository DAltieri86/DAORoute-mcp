# Security Policy

DaoRoute is designed as a non-custodial decision layer.

## Do Not Share

Never publish or submit:

- MCP API keys;
- wallet private keys or seed phrases;
- model artifacts;
- database dumps;
- production `.env` files;
- raw logs containing client identifiers;
- hosted endpoint secrets.

## Supported Pilot Auth

Pilot users authenticate with an API key supplied through one of:

- MCP request metadata: `api_key`;
- HTTP header: `x-api-key`;
- HTTP header: `Authorization: Bearer <key>`.

## Reporting Security Issues

Email:

```text
softwaretamrsv@gmail.com
```

Use the subject:

```text
DaoRoute Security Report
```

Do not open public issues containing secrets, exploit details, API keys, or
private endpoint information.

