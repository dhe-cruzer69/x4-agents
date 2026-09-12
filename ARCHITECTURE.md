# x4-agents Architecture

## Flagship role

x4-agents is the primary user-facing product of the X4 ecosystem. It provides secure, observable, policy-controlled multi-agent orchestration.

It builds on the security and approval concepts first explored in [ariexus](https://github.com/dhe-cruzer69/ariexus).

## High-level execution graph

```
USER
 │
 ▼
Task Interface
 │
 ▼
Planner
 │
 ▼
Task Graph
 ├── Research Agent
 ├── Coding Agent
 └── Browser Agent
 │
Policy Engine → Risk Classification
 ├─ ALLOW
 └─ APPROVAL REQUIRED
 │
Tool Runtime (x4-sandbox + x4-mcp-gateway)
 │
Memory (x4-memory) → Verification → Result → Audit
```

## Security chain (non-negotiable)

```
Agent Intent
    ↓
Policy Engine
    ↓
Risk Score (LOW / MEDIUM / HIGH)
    ↓
Permission Check
    ↓
Human Approval (if required)
    ↓
Sandbox Execution
    ↓
Immutable Audit Event
```

Agents never receive unrestricted production credentials.

## Module map (target)

```
x4-agents/
├── planner/
├── graph/
├── runtime/
├── agents/
│   ├── research/
│   ├── coding/
│   ├── browser/
│   └── general/
├── tools/
├── permissions/
├── approvals/
├── execution/
├── memory/
├── verification/
├── audit/
└── cli/
```

## Dependencies on other X4 packages

- x4-core — config, logging, events, permissions
- x4-ai — model inference & tool calling
- x4-memory — persistent state
- x4-sandbox — isolated tool execution
- x4-mcp-gateway — controlled external tools
