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

    def to_dict(self) -> dict:
        """
        Convert the task into a dictionary for persistent storage.
        """

        return {
            "id": self.id,
            "goal": self.goal,
            "status": self.status.value,
            "parent_task_id": self.parent_task_id,
            "dependencies": self.dependencies,
            "result": self.result,
            "error": self.error,
            "attempts": self.attempts,
        }
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Reconstruct a Task object from stored dictionary data.
        """

        return cls(
            id=data["id"],
            goal=data["goal"],
            status=TaskStatus(data.get("status", "pending")),
            parent_task_id=data.get("parent_task_id"),
            result=data.get("result"),
            error=data.get("error"),
            attempts=data.get("attempts", 0),
            subtasks=data.get("subtasks", []),
            dependencies=data.get("dependencies", []),
        )