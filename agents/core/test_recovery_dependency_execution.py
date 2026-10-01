from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_dependency_execution.json"

print("\nTesting recovered dependency execution...\n")

memory = Memory(MEMORY_FILE)

# Dependency task
research_task = Task(
    id="research-task",
    goal="Research Python",
)

research_task.status = TaskStatus.COMPLETED
research_task.result = "Python research completed"

memory.store_task(research_task)


# Dependent task that was interrupted
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

print("Recovered task:")
print(recovered_tasks[0])


# Check dependency state before execution
dependency_state = orchestrator.memory.get_task("research-task")

if dependency_state["status"] == "completed":
    print("\nDependency is completed.")
else:
    print("\nFAIL: Dependency is not completed.")


# Resume the dependent task
orchestrator.resume_incomplete_tasks()

updated_task = orchestrator.memory.get_task("analysis-task")

print("\nUpdated dependent task:")
print(updated_task)


if (
    updated_task["status"] == "completed"
    and dependency_state["status"] == "completed"
):
    print("\nPASS: Recovered task executed with completed dependency.")
else:
    print("\nFAIL: Dependency execution check failed.")