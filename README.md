# x4-agents

**Flagship secure multi-agent orchestration runtime**

Task graphs • sandboxed tools • approvals • audit • memory • MCP

## Vision

x4-agents is the center of the X4 ecosystem. It evolves concepts from the existing `ariexus` prototype into a production-oriented agent harness with strong security boundaries.

```
USER → Planner → Task Graph → Agents (Research / Code / Browser)
         ↓
    Tool Runtime (x4-ai + x4-mcp-gateway + x4-sandbox)
         ↓
    Policy → Approval → Execution → Audit → Memory → Verification → Result
```

## Non-negotiable controls

- Every tool call goes through policy evaluation
- High-risk actions require human approval
- Immutable audit log
- Sandbox isolation for execution
- Cost and permission tracking

## Status

Foundation stage. Architecture and security model defined. Implementation in progress, seeded from ariexus patterns.

## Relationship to ariexus

`ariexus` remains the historical prototype. Mature modules (task models, approval, audit, sandboxed tools) will be ported and improved here while preserving attribution.

## Quick links

- [SECURITY.md](SECURITY.md)
- [ROADMAP.md](ROADMAP.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

## License

Apache-2.0

---

Part of the [X4 ecosystem](https://github.com/dhe-cruzer69) by ARIEX4Ops.
