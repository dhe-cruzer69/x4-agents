# Security Policy

Agent runtimes are high-risk software. We take security seriously.

## Reporting

Use GitHub Security Advisories. Do not open public issues for vulnerabilities.

## Design Principles

- No unrestricted production credentials for agents
- Every tool call passes through policy + permission + sandbox
- Immutable audit log of all tool invocations
- Human approval required for high-risk actions
- Resource limits and timeouts by default
