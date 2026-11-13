# Power Automate cloud-flow blueprint

This is an implementation guide, not an importable Power Platform solution. Connector/API availability depends on tenant licensing, environment configuration, and permissions.

## SW-01 — Failure Event Collector
1. Trigger from an approved source failure branch or scheduled run-history poller.
2. Capture environment, flow ID, run ID, failed action, timestamps, and sanitized error.
3. Build stable `sourceEventKey` from environment + flow ID + run ID.
4. Upsert an Incident row in Dataverse; increment occurrence count for duplicates.
5. Create a Failure Event row and invoke SW-02.
6. Log correlation ID and outcome. Never log secrets or raw PHI payloads.

## SW-02 — Investigation Orchestrator
1. Retrieve run/action metadata and approved diagnostic evidence.
2. Retrieve verified knowledge-base matches.
3. Call Investigation Agent using `investigation-request.v1`.
4. Validate response against `investigation-response.v1`.
5. Persist diagnosis, evidence references, confidence, and agent version.
6. Invoke SW-03.

## SW-03 — Policy Router
- `business_exception` → Finance/process owner; never Coding Agent.
- `credentials` → connection owner/platform support; never expose secret details.
- `timeout` → recovery review; check idempotency, transaction state, retry-after, and retry budget.
- `system_error` → coding proposal only with strong evidence, confidence threshold, and repository mapping.
- `unknown` / low confidence → human review.

## SW-04 — Controlled Recovery
Require an allowlisted action, idempotency key, transaction-state check, bounded attempts, cooldown, and audit record. Do not automatically retry invoice submission unless it is proven safe and idempotent.

## SW-05 — Notifications
Send a Teams card with incident ID, flow, severity, classification, confidence, and evidence summary. Approval buttons must call a server-side flow that revalidates user identity and policy.

Use a managed solution, connection references, environment variables, and Key Vault for secrets. Do not store secrets in plain-text environment variables.
