# SpectreWatch reference architecture

```mermaid
flowchart TD
 A[Power Automate Cloud / PAD] --> B[Failure detector]
 B --> C[Normalize and redact event]
 C --> D[(Dataverse incident store)]
 D --> E[Investigation agent]
 E --> F[Deterministic policy router]
 F -->|Business exception| G[Finance / process owner]
 F -->|Credentials| H[Connection owner]
 F -->|Timeout| I[Recovery review]
 F -->|Confirmed code defect| J[Coding Agent proposal]
 F -->|Unknown / low confidence| K[Human review]
 J --> L[Draft PR + tests]
 L --> M[Human approval]
```

## Components
1. **Telemetry:** approved Power Automate run-history sources, PAD execution results, and dependency status.
2. **Collector:** normalize platform errors into `failure-event.v1`; deduplicate by environment + flow + run ID.
3. **Dataverse:** automation registry, incidents, failure events, investigations, remediation actions, and knowledge articles.
4. **Investigation:** retrieve sanitized evidence and verified knowledge matches; return classification, evidence, confidence, and recommended action.
5. **Policy router:** deterministic rules take precedence over model suggestions.
6. **Remediation:** notify, create ticket, or allowlisted idempotent recovery. Coding Agent proposes a branch/draft PR only.
7. **Experience:** Power Apps incident dashboard and Teams adaptive-card notifications.

## Design principles
Platform-neutral event schema, least privilege, data minimization, idempotency, bounded retries, auditability, and human approval for production-impacting changes.
