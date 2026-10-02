from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_dependency_blocking_execution.json"

print("\nTesting recovery dependency blocking...\n")

memory = Memory(MEMORY_FILE)


# Create the dependent task FIRST.
# This makes it appear first during recovery.
analysis_task = Task(
    id="analysis-task",
    goal="Analyze Python research",
)

analysis_task.status = TaskStatus.RUNNING
analysis_task.attempts = 1
analysis_task.dependencies = ["research-task"]

memory.store_task(analysis_task)


# Create its incomplete dependency SECOND.
research_task = Task(
    id="research-task",
    goal="Research Python",
)

research_task.status = TaskStatus.RUNNING
research_task.attempts = 1

memory.store_task(research_task)


# Simulate restart
orchestrator = Orchestrator()
orchestrator.memory = Memory(MEMORY_FILE)

print("Resuming recovered tasks...\n")

orchestrator.resume_incomplete_tasks()


analysis_state = orchestrator.memory.get_task("analysis-task")
research_state = orchestrator.memory.get_task("research-task")

print("Analysis task state:")
print(analysis_state)

print("\nResearch task state:")
print(research_state)


history = orchestrator.memory.get_history()

print("\nExecution history:")
print(history)

if (
    analysis_state["status"] == "completed"
    and research_state["status"] == "completed"
    and history.index("research-task")
    < history.index("analysis-task")
):
    print(
        "\nPASS: Dependency was completed "
        "before the dependent task."
    )
else:
    print(
        "\nFAIL: Dependent task executed before "
        "its dependency."
    )