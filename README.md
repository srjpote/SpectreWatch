# SpectreWatch
**Monitor. Investigate. Recover.**

SpectreWatch is an AI-powered automation monitoring and intelligent failure-remediation reference project. Milestone 1 focuses on hybrid Microsoft Power Automate cloud flows and Power Automate Desktop (PAD), using invoice processing to demonstrate failure capture, investigation, safe routing, and human-governed remediation.

## Included
- Architecture and Power Automate cloud-flow implementation blueprint
- Dataverse logical data model
- Versioned JSON contracts for failure events and agent integrations
- Local invoice-processing simulator with five scenarios
- Deterministic policy router and automated tests
- Security/privacy guidance and implementation backlog

## Run locally
Requires Python 3.10+.
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
spectrewatch --scenario application_null_tax
pytest
```
Without installing:
```bash
PYTHONPATH=src python -m spectrewatch.cli --scenario business_approval_limit
```

## Scenarios
`success`, `application_null_tax`, `business_approval_limit`, `system_timeout`, `credential_failure`.

## Important scope note
This is a local reference implementation and build blueprint, not an imported/deployed Power Platform solution. It does not connect to Dataverse, PAD, Power Automate, Azure OpenAI, GitHub, or production invoice systems. Tenant-specific connectors and credentials must be configured separately.

## Safety principles
- Never send credentials, tokens, or secrets to an AI model.
- Minimize and redact PHI/PII before logging or investigation.
- Never blindly retry non-idempotent financial operations.
- Business exceptions go to business owners, never the Coding Agent.
- Coding Agent creates draft PR proposals only; require tests and human approval before merge/deployment.
- Validate agent output and use deterministic policy rules for actions.
