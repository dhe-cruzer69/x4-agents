# Security Policy — x4-agents

## Threat model (high level)

- Prompt injection leading to unintended tool use
- Privilege escalation via tool permissions
- Sandbox escape
- Secret leakage through tool arguments or logs
- Audit log tampering
- Supply-chain compromise of dependencies

## Reporting

Report vulnerabilities privately (GitHub security advisory preferred). Do not open public issues for security problems.

## Design principles

1. Least privilege by default
2. Explicit human approval for high-risk actions
3. All tool invocations audited
4. Execution only inside approved sandbox boundaries
5. No unrestricted production credentials for autonomous agents
