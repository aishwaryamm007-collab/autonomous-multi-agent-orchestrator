from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus


print("\n========== TASK STATE MEMORY TEST ==========")

file_path = "test_task_state.json"

memory = Memory(file_path)

task = Task(
    id="state-001",
    goal="Test complete task state",
)

task.status = TaskStatus.COMPLETED
task.result = "Task completed successfully."
task.attempts = 2
task.dependencies = [
    "state-000"
]

memory.store_task(task)

print("\nTask stored in memory.")


# ---------------------------------------------
# Retrieve task state
# ---------------------------------------------

stored_task = memory.get_task("state-001")

if stored_task:
    print("Task state retrieval: PASS")
else:
    print("Task state retrieval: FAIL")


# ---------------------------------------------
# Validate stored fields
# ---------------------------------------------

if stored_task["status"] == "completed":
    print("Status persistence: PASS")
else:
    print("Status persistence: FAIL")

if stored_task["result"] == "Task completed successfully.":
    print("Result persistence: PASS")
else:
    print("Result persistence: FAIL")

if stored_task["attempts"] == 2:
    print("Attempts persistence: PASS")
else:
    print("Attempts persistence: FAIL")

if stored_task["dependencies"] == ["state-000"]:
    print("Dependencies persistence: PASS")
else:
    print("Dependencies persistence: FAIL")


# ---------------------------------------------
# Verify JSON reload
# ---------------------------------------------

new_memory = Memory(file_path)

reloaded_task = new_memory.get_task("state-001")

if reloaded_task:
    print("Task state reload: PASS")
else:
    print("Task state reload: FAIL")


print("\nStored task state:")
print(reloaded_task)

print("\n========== TEST COMPLETE ==========")