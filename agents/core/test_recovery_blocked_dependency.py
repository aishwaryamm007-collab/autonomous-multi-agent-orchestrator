from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_blocked_dependency.json"

print("\nTesting blocked dependency recovery...\n")

memory = Memory(MEMORY_FILE)

# Incomplete dependency
research_task = Task(
    id="research-task",
    goal="Research Python",
)

research_task.status = TaskStatus.RUNNING
research_task.attempts = 1

memory.store_task(research_task)


# Dependent task
analysis_task = Task(
    id="analysis-task",
    goal="Analyze Python research",
)

analysis_task.status = TaskStatus.RUNNING
analysis_task.attempts = 1
analysis_task.dependencies = ["research-task"]

memory.store_task(analysis_task)


# Simulate restart
orchestrator = Orchestrator()
orchestrator.memory = Memory(MEMORY_FILE)

recovered_tasks = orchestrator.recover_tasks()

print("Recovered tasks:")

for task in recovered_tasks:
    print(task)


# At this stage both tasks are recoverable,
# but analysis must wait for research.
research_state = orchestrator.memory.get_task("research-task")

analysis_task_recovered = next(
    task
    for task in recovered_tasks
    if task.id == "analysis-task"
)

if (
    research_state["status"] != "completed"
    and "research-task" in analysis_task_recovered.dependencies
):
    print("\nPASS: Dependent task has an incomplete dependency.")
else:
    print("\nFAIL: Dependency state was not detected correctly.")