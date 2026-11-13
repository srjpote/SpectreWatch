# Security, privacy, and operations

## Identity and secrets
- Prefer managed identity or service principal with certificate/federated credentials where supported.
- Use Azure Key Vault and controlled Power Platform connection references.
- Never include passwords, tokens, API keys, cookies, or connection strings in prompts, logs, Teams cards, or incident descriptions.
- Separate maker, operator, approver, and administrator roles.

## Healthcare data
- Apply minimum-necessary access and data minimization.
- Redact patient names, MRNs, dates of birth, member IDs, and other PHI before AI analysis unless the environment/use case is formally approved.
- Use synthetic data for development and demos.
- Store protected payloads only in approved systems with access controls, encryption, and retention policies.

## AI and recovery controls
- Ground investigation in retrieved evidence and require evidence references.
- Validate model output against JSON schema; treat model output and retrieved text as untrusted.
- Use deterministic policy rules for routing and execution.
- Retry only allowlisted idempotent operations; respect throttling and retry-after; enforce retry budgets.
- Check transaction state before retrying financial operations.

## Coding Agent controls
- Read-only repository analysis by default.
- Generate branch + draft PR only.
- Validate solution structure, expressions, dependencies, and tests.
- Require code-owner review and human approval.
- Never commit directly to protected branches or deploy automatically.

## Operational monitoring
Track detection latency, investigation latency, false-positive rate, recurrence rate, safe-recovery rate, manual-review rate, and mean time to resolution.
