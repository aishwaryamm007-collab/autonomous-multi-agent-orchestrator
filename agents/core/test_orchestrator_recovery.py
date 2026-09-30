from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


print("\nTesting Orchestrator recovery...\n")

orchestrator = Orchestrator()

# Use a separate test memory file
orchestrator.memory = Memory("test_orchestrator_recovery.json")

# Create an incomplete task
task = Task(
    id="recovery-task-1",
    goal="Test recovery",
)

task.status = TaskStatus.RUNNING
task.attempts = 1

# Store the incomplete task
orchestrator.memory.store_task(task)

# Get incomplete tasks
incomplete_tasks = orchestrator.get_incomplete_tasks()

print("Incomplete tasks:")
print(incomplete_tasks)

# Verify the task was detected
if "recovery-task-1" in incomplete_tasks:
    print("\nPASS: Incomplete task detected.")
else:
    print("\nFAIL: Incomplete task was not detected.")