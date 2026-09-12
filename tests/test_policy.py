"""Policy engine tests."""

from x4.agents import PolicyEngine, RiskLevel


def test_low_risk() -> None:
    engine = PolicyEngine()
    d = engine.evaluate("read", "./file.txt")
    assert d.allowed is True
    assert d.risk == RiskLevel.LOW
    assert d.requires_approval is False


def test_high_risk_requires_approval() -> None:
    engine = PolicyEngine()
    d = engine.evaluate("delete", "/important")
    assert d.requires_approval is True
    assert d.risk == RiskLevel.HIGH
