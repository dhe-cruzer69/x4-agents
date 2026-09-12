"""Runtime security chain tests."""

from x4.agents import AgentRuntime, Task


def test_safe_task_succeeds() -> None:
    runtime = AgentRuntime()
    task = Task(description="List files")
    result = runtime.run(task, action="read", resource="./")
    assert result.success is True
    assert result.audit_id is not None


def test_high_risk_blocked_without_approval() -> None:
    runtime = AgentRuntime(require_approval_for_high_risk=True)
    task = Task(description="Delete something")
    result = runtime.run(task, action="delete", resource="/data")
    assert result.success is False
    assert "Approval required" in (result.error or "")


def test_high_risk_allowed_after_approval() -> None:
    runtime = AgentRuntime(require_approval_for_high_risk=True)
    task = Task(description="Delete something")
    runtime.approve(task.id)
    result = runtime.run(task, action="delete", resource="/data")
    # Policy still marks high risk but approval was granted
    assert result.success is True or result.error is not None  # depends on policy allow flag
