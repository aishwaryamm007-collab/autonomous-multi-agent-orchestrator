from agents.core.models import TaskStatus
from agents.core.task_manager import TaskManager


manager = TaskManager()

task = manager.create_task(
    "task-001",
    "Research Python and Java",
)

print("Created:", task)

manager.update_status(
    "task-001",
    TaskStatus.RUNNING,
)

updated_task = manager.get_task("task-001")

print("Updated:", updated_task)
print("Current status:", updated_task.status.value)