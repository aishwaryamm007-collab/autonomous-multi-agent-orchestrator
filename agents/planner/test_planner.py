from agents.core.llm_service import LLMService
from agents.core.models import Task
from agents.planner.planner import PlannerAgent


task = Task(
    id="task-001",
    goal="Research Python and Java",
)

llm_service = LLMService()

planner = PlannerAgent(llm_service)

subtasks = planner.plan(task)

print("Generated subtasks:")

for subtask in subtasks:
   print(
    f"- {subtask.id}: {subtask.goal} "
    f"| dependencies: {subtask.dependencies}"
)

print("\nSubtask IDs stored in main task:")
print(task.subtasks)