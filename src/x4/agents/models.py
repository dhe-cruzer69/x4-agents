"""Core task models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class Task:
    """A unit of work for an agent."""

    description: str
    id: str = field(default_factory=lambda: str(uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class TaskResult:
    """Result of a task execution."""

    task_id: str
    success: bool
    output: Any = None
    error: str | None = None
    audit_id: str | None = None
