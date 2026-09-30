from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


print("\nTesting Orchestrator task recovery...\n")

orchestrator = Orchestrator()

# Use separate test memory
orchestrator.memory = Memory("test_task_recovery_orchestrator.json")

# Create an incomplete task
task = Task(
    id="recovered-task-1",
    goal="Test recovering an incomplete task",
)

task.status = TaskStatus.RUNNING
task.attempts = 2
task.dependencies = ["previous-task"]

# Store it
orchestrator.memory.store_task(task)

# Recover incomplete tasks
recovered_tasks = orchestrator.recover_tasks()

print("Recovered tasks:")
for recovered_task in recovered_tasks:
    print(recovered_task)

if (
    len(recovered_tasks) == 1
    and recovered_tasks[0].id == "recovered-task-1"
    and recovered_tasks[0].status == TaskStatus.PENDING
    and recovered_tasks[0].attempts == 2
    and recovered_tasks[0].dependencies == ["previous-task"]
):
    print("\nPASS: Task recovered successfully.")
else:
    print("\nFAIL: Task recovery failed.")