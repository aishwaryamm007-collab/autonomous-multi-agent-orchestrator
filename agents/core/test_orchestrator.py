from agents.core.models import Task
from agents.core.orchestrator import Orchestrator


task = Task(
    id="workflow-001",
    goal="Research Python and Java",
)

orchestrator = Orchestrator()

final_result = orchestrator.execute(task)

print("\n\n========== FINAL OUTPUT ==========")
print(final_result)
print("==================================")
