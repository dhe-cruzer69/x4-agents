"""Immutable audit log."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class AuditEvent:
    id: str
    action: str
    actor: str
    resource: str
    allowed: bool
    risk: str
    timestamp: datetime
    details: dict[str, Any] = field(default_factory=dict)


class AuditLog:
    """In-memory audit log (replace with durable store in production)."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(
        self,
        action: str,
        actor: str,
        resource: str,
        allowed: bool,
        risk: str,
        details: dict[str, Any] | None = None,
    ) -> str:
        event_id = str(uuid4())
        event = AuditEvent(
            id=event_id,
            action=action,
            actor=actor,
            resource=resource,
            allowed=allowed,
            risk=risk,
            timestamp=datetime.now(timezone.utc),
            details=details or {},
        )
        self._events.append(event)
        return event_id

    def list_events(self) -> list[AuditEvent]:
        return list(self._events)
