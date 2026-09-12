# Security Policy — x4-agents

## Reporting

Do not open public issues for vulnerabilities. Use private reporting.

## Threat model focus

- Prompt injection leading to tool abuse
- Privilege escalation via tools
- Secret leakage
- Filesystem / network escape from sandbox
- Audit log tampering
- Supply-chain compromise of tools

Agents must never receive unrestricted production credentials.
