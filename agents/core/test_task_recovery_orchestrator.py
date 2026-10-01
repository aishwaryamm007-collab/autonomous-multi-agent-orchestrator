from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


print("\nTesting Orchestrator task recovery and resume...\n")

orchestrator = Orchestrator()

# Use separate test memory
orchestrator.memory = Memory("test_task_recovery_orchestrator.json")

# Create an incomplete task
task = Task(
    id="recovered-task-1",
    goal="Analyze a simple topic",
)

task.status = TaskStatus.RUNNING
task.attempts = 1

# Store incomplete task
orchestrator.memory.store_task(task)

print("Stored incomplete task.")

# Resume incomplete tasks
recovered_tasks = orchestrator.resume_incomplete_tasks()

print("\nRecovered and resumed tasks:")

for recovered_task in recovered_tasks:
    print(recovered_task)

# Verify recovery
if len(recovered_tasks) == 1:
    print("\nPASS: Incomplete task was recovered and resume was triggered.")
else:
    print("\nFAIL: Task recovery failed.")