# x4-agents

**Flagship secure multi-agent orchestration runtime**

Task graphs • sandboxed tools • approval gates • audit logging • memory • MCP

Built as the evolution of the ariexus prototype.

## Vision

Provide a production-oriented agent harness where every tool call is policy-checked, optionally human-approved, sandboxed, and fully audited.

## Architecture (high level)

```
USER → Task Interface → Planner → Task Graph
         ↓
   Research / Coding / Browser Agents
         ↓
   Tool Runtime (x4-sandbox + x4-mcp-gateway)
         ↓
   Policy → Permission → Approval → Execution → Audit
         ↓
   Memory (x4-memory) → Verification → Result
```

## Status

Foundation stage. Core concepts and structure are being established. Not production-ready.

## Related Projects

- [x4-core](https://github.com/dhe-cruzer69/x4-core)
- [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox)
- [x4-mcp-gateway](https://github.com/dhe-cruzer69/x4-mcp-gateway)
- [x4-memory](https://github.com/dhe-cruzer69/x4-memory)
- [ariexus](https://github.com/dhe-cruzer69/ariexus) (prototype ancestor)

## Security

See [SECURITY.md](SECURITY.md). High-risk actions require explicit policy and optional human approval.

## License

Apache-2.0
