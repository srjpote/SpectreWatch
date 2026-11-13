# Dataverse logical data model

Use publisher prefix `sw_`; adapt names to organizational standards.

| Table | Suggested columns |
|---|---|
| Automation | name, platform, environment ID, external automation ID, owner team, repository URL, active |
| Incident | autonumber, title, automation lookup, status, severity, classification, source event key (alternate key), first/last seen, occurrence count, correlation ID, assigned team, sanitized summary |
| Failure Event | incident lookup, source platform, flow run ID, failed action, error code, redacted message, timestamp, protected payload pointer, payload hash |
| Investigation | incident lookup, agent version, classification, root cause, confidence, evidence JSON, recommended action, created on |
| Remediation Action | incident lookup, action type, status, idempotency key, approver, approval timestamp, execution result |
| Knowledge Article | title, symptom, root cause, resolution, classification, automation lookup, verified, last validated |

Relationships: Automation 1:N Incident; Incident 1:N Failure Event, Investigation, and Remediation Action; Knowledge Article optionally N:1 Automation.

Suggested alternate keys: Incident `sourceEventKey`; Automation platform + environment + external ID. Store only sanitized diagnostic data in Dataverse. Keep PHI/raw logs in an approved protected store with retention controls.
