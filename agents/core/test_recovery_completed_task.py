from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_completed_task.json"

print("\nTesting completed-task recovery protection...\n")

memory = Memory(MEMORY_FILE)

# Completed task
completed_task = Task(
    id="completed-task",
    goal="Already completed task",
)

completed_task.status = TaskStatus.COMPLETED
completed_task.result = "Already finished"

memory.store_task(completed_task)

# Incomplete task
incomplete_task = Task(
    id="incomplete-task",
    goal="Task that needs recovery",
)

incomplete_task.status = TaskStatus.RUNNING
incomplete_task.attempts = 1

memory.store_task(incomplete_task)

# Simulate a new program run
orchestrator = Orchestrator()
orchestrator.memory = Memory(MEMORY_FILE)

recovered_tasks = orchestrator.recover_tasks()

print("Recovered tasks:")

for task in recovered_tasks:
    print(task.id)

if (
    len(recovered_tasks) == 1
    and recovered_tasks[0].id == "incomplete-task"
):
    print("\nPASS: Completed task was not recovered.")
else:
    print("\nFAIL: Completed task was incorrectly recovered.")