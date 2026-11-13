# PAD invoice performer contract

## Input
```json
{
  "correlationId": "guid",
  "invoiceId": "INV-10001",
  "vendorId": "VEND-001",
  "amount": 1250.00,
  "taxAmount": 125.00,
  "scenario": "success"
}
```

## Output
```json
{
  "correlationId": "guid",
  "invoiceId": "INV-10001",
  "status": "Completed",
  "total": 1375.00,
  "errorType": null,
  "errorMessage": null,
  "retryable": false
}
```

## Desktop flow stages
1. Validate required inputs and data types.
2. Retrieve vendor approval limit from an approved source.
3. Validate invoice amount against the limit.
4. Calculate amount + tax.
5. Submit or stage invoice in the target system.
6. Return a structured result to the cloud flow.
7. On exception, return a sanitized error category/message; cloud flow creates the canonical failure event.

## Failure simulation
- `application_null_tax`: missing tax value; fail validation rather than silently coercing to zero.
- `business_approval_limit`: invoice amount exceeds vendor approval limit.
- `system_timeout`: downstream dependency timeout.
- `credential_failure`: connection unauthorized; never expose credential details.

For financial actions, use a transaction idempotency key and verify whether the invoice was already submitted before retrying.
