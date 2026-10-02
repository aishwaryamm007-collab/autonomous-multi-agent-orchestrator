from agents.core.memory import Memory
from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


MEMORY_FILE = "test_recovery_deadlock.json"

print("\nTesting recovery deadlock protection...\n")

memory = Memory(MEMORY_FILE)

# Task A depends on Task B
task_a = Task(
    id="task-a",
    goal="Task A",
)

task_a.status = TaskStatus.RUNNING
task_a.dependencies = ["task-b"]

memory.store_task(task_a)


# Task B depends on Task A
task_b = Task(
    id="task-b",
    goal="Task B",
)

task_b.status = TaskStatus.RUNNING
task_b.dependencies = ["task-a"]

memory.store_task(task_b)


# Simulate restart
orchestrator = Orchestrator()
orchestrator.memory = Memory(MEMORY_FILE)

print("Attempting recovery...\n")

recovered_tasks = orchestrator.resume_incomplete_tasks()

print("\nRecovered tasks:")

for task in recovered_tasks:
    print(task)


task_a_state = orchestrator.memory.get_task("task-a")
task_b_state = orchestrator.memory.get_task("task-b")

print("\nFinal states:")
print("Task A:", task_a_state)
print("Task B:", task_b_state)


if (
    task_a_state["status"] != "completed"
    and task_b_state["status"] != "completed"
):
    print("\nPASS: Recovery stopped safely on dependency deadlock.")
else:
    print("\nFAIL: Deadlocked tasks were executed.")