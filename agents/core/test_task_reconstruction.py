from agents.core.models import Task, TaskStatus


print("\nTesting Task reconstruction...\n")

stored_task = {
    "id": "recovery-task-1",
    "goal": "Test task reconstruction",
    "status": "running",
    "parent_task_id": None,
    "dependencies": ["task-1"],
    "result": None,
    "error": None,
    "attempts": 2,
}

task = Task.from_dict(stored_task)

print("Reconstructed task:")
print(task)

if (
    task.id == "recovery-task-1"
    and task.status == TaskStatus.RUNNING
    and task.attempts == 2
    and task.dependencies == ["task-1"]
):
    print("\nPASS: Task reconstructed successfully.")
else:
    print("\nFAIL: Task reconstruction failed.")
    