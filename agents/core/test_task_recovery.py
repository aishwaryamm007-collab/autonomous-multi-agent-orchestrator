from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus


print("\n========== TASK RECOVERY TEST ==========")

file_path = "test_recovery.json"

memory = Memory(file_path)


# ---------------------------------------------
# Create an incomplete task
# ---------------------------------------------

task = Task(
    id="recovery-001",
    goal="Test recovery after restart",
)

task.status = TaskStatus.RUNNING
task.attempts = 1

memory.store_task(task)

print("\nIncomplete task stored.")


# ---------------------------------------------
# Simulate application restart
# ---------------------------------------------

new_memory = Memory(file_path)

incomplete_tasks = new_memory.get_incomplete_tasks()

print("\nIncomplete tasks found:")
print(incomplete_tasks)


# ---------------------------------------------
# Validate recovery
# ---------------------------------------------

if "recovery-001" in incomplete_tasks:
    print("Incomplete task detection: PASS")
else:
    print("Incomplete task detection: FAIL")


if (
    incomplete_tasks["recovery-001"]["status"]
    == "running"
):
    print("Task status recovery: PASS")
else:
    print("Task status recovery: FAIL")


if (
    incomplete_tasks["recovery-001"]["attempts"]
    == 1
):
    print("Task attempts recovery: PASS")
else:
    print("Task attempts recovery: FAIL")


print("\n========== TEST COMPLETE ==========")