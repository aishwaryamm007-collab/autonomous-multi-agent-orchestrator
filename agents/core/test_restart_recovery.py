from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_restart_recovery.json"


print("\nTesting recovery across a simulated restart...\n")


# --------------------------------------------------
# Phase 1: First program run
# --------------------------------------------------

print("PHASE 1: Creating incomplete task...")

memory = Memory(MEMORY_FILE)

task = Task(
    id="restart-task-1",
    goal="Analyze a simple topic",
)

task.status = TaskStatus.RUNNING
task.attempts = 1

memory.store_task(task)

print("Incomplete task saved to JSON.")


# --------------------------------------------------
# Phase 2: Simulate program restart
# --------------------------------------------------

print("\nPHASE 2: Starting a new Orchestrator...")

orchestrator = Orchestrator()

# Load the same persistent memory file
orchestrator.memory = Memory(MEMORY_FILE)

recovered_tasks = orchestrator.recover_tasks()

print("\nRecovered tasks:")

for recovered_task in recovered_tasks:
    print(recovered_task)


# --------------------------------------------------
# Verify recovery
# --------------------------------------------------

if (
    len(recovered_tasks) == 1
    and recovered_tasks[0].id == "restart-task-1"
    and recovered_tasks[0].status == TaskStatus.PENDING
):
    print("\nPASS: Task recovered after simulated restart.")
else:
    print("\nFAIL: Task was not recovered correctly.")


# --------------------------------------------------
# Phase 3: Resume the recovered task
# --------------------------------------------------

print("\nPHASE 3: Resuming recovered task...")

orchestrator.resume_incomplete_tasks()

updated_task = orchestrator.memory.get_task("restart-task-1")

print("\nUpdated task state:")
print(updated_task)


if updated_task["status"] == "completed":
    print("\nPASS: Task completed after restart recovery.")
else:
    print("\nFAIL: Task did not complete after recovery.")