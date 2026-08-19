from agents.core.models import Task
from agents.planner.planner import PlannerAgent


task = Task(
    id="task-001",
    goal="Research Python and Java",
)

planner = PlannerAgent()

subtasks = planner.plan(task)

print("Main task:")
print(task)

print("\nGenerated subtasks:")

for subtask in subtasks:
    print(f"- {subtask.id}: {subtask.goal}")

print("\nSubtask IDs stored in main task:")
print(task.subtasks)