# x4-agents

**Flagship secure multi-agent orchestration runtime**

Task graphs • Sandboxed tools • Approvals • Audit • Memory • MCP

Built on the concepts pioneered in [ariexus](https://github.com/dhe-cruzer69/ariexus).

Part of [ARIEX4Ops / X4](https://github.com/dhe-cruzer69).

## Vision

```
USER TASK
    │
    ▼
 PLANNER → TASK GRAPH
    │
    ├─ Research Agent
    ├─ Coding Agent
    └─ Browser Agent
    │
 TOOL RUNTIME (x4-sandbox + x4-mcp-gateway)
    │
 POLICY → PERMISSION → APPROVAL → AUDIT
    │
 MEMORY (x4-memory) → VERIFICATION → RESULT
```

## Security model (non-negotiable)

- No unrestricted production credentials for agents
- Explicit policy + risk classification before tool use
- Human approval gates for high-risk actions
- Immutable audit log of tool calls
- Sandboxed execution by default

## Status

v0.1 foundation. Evolving from ariexus MVP.

## Related

- [x4-core](https://github.com/dhe-cruzer69/x4-core)
- [x4-ai](https://github.com/dhe-cruzer69/x4-ai)
- [x4-sandbox](https://github.com/dhe-cruzer69/x4-sandbox)
- [x4-mcp-gateway](https://github.com/dhe-cruzer69/x4-mcp-gateway)
- [x4-memory](https://github.com/dhe-cruzer69/x4-memory)

## License

Apache-2.0

## Support

[GitHub Sponsors](https://github.com/sponsors/dhe-cruzer69)
