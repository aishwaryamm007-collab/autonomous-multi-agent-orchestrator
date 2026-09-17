from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


print("\n========== MEMORY INTEGRATION TEST ==========")

task = Task(
    id="memory-001",
    goal="Research Python and Java",
)

orchestrator = Orchestrator()

result = orchestrator.execute(task)

print("\n========== VALIDATING MEMORY ==========")

memory_results = orchestrator.memory.get_all_results()

if memory_results:
    print("Results stored in memory: PASS")
else:
    print("Results stored in memory: FAIL")

if task.status == TaskStatus.COMPLETED:
    print("Workflow completed: PASS")
else:
    print(f"Workflow completed: FAIL ({task.status})")

print("\nStored task results:")

for task_id, task_result in memory_results.items():
    print(f"- {task_id}: {task_result}")

print("\n========== TEST COMPLETE ==========")