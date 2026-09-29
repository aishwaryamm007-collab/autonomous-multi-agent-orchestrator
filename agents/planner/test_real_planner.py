from agents.core.models import Task
from agents.core.llm_service import LLMService
from agents.planner.planner import PlannerAgent


print("\n========== REAL PLANNER TEST ==========")

llm_service = LLMService()
planner = PlannerAgent(llm_service)

task = Task(
    id="planner-001",
    goal="Build a machine learning application",
)

subtasks = planner.plan(task)

print("\nGenerated subtasks:")

for subtask in subtasks:
    print(f"\nID: {subtask.id}")
    print(f"Goal: {subtask.goal}")
    print(f"Dependencies: {subtask.dependencies}")

if subtasks:
    print("\nPlanner generated subtasks: PASS")
else:
    print("\nPlanner generated subtasks: FAIL")

print("\n========== TEST COMPLETE ==========")