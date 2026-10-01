from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_dependencies.json"

print("\nTesting recovery with dependencies...\n")

memory = Memory(MEMORY_FILE)

# Completed dependency
research_task = Task(
    id="research-task",
    goal="Research information",
)

research_task.status = TaskStatus.COMPLETED
research_task.result = "Research completed"

memory.store_task(research_task)


# Incomplete dependent task
analysis_task = Task(
    id="analysis-task",
    goal="Analyze the research",
)

analysis_task.status = TaskStatus.RUNNING
analysis_task.attempts = 1
analysis_task.dependencies = ["research-task"]

memory.store_task(analysis_task)


# Simulate program restart
orchestrator = Orchestrator()
orchestrator.memory = Memory(MEMORY_FILE)

recovered_tasks = orchestrator.recover_tasks()

print("Recovered tasks:")

for task in recovered_tasks:
    print(task)


if (
    len(recovered_tasks) == 1
    and recovered_tasks[0].id == "analysis-task"
    and recovered_tasks[0].status == TaskStatus.PENDING
    and recovered_tasks[0].dependencies == ["research-task"]
):
    print("\nPASS: Dependent task recovered correctly.")
else:
    print("\nFAIL: Dependency recovery failed.")