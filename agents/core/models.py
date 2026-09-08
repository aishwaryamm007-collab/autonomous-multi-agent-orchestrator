from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(BaseModel):
    id: str
    goal: str
    status: TaskStatus = TaskStatus.PENDING
    parent_task_id: str | None = None
    result: Any | None = None
    error: str | None = None
    attempts: int = 0
    subtasks: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)