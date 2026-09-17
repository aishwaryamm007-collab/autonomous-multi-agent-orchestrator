from agents.core.models import Task, TaskStatus
from agents.core.orchestrator import Orchestrator


print("\n========== FULL WORKFLOW TEST ==========")

task = Task(
    id="integration-001",
    goal="Build a machine learning application",
)

orchestrator = Orchestrator()

result = orchestrator.execute(task)

print("\n========== VALIDATING RESULT ==========")

# Check final task status
if task.status == TaskStatus.COMPLETED:
    print("Final task status: PASS")
else:
    print(f"Final task status: FAIL ({task.status})")

# Check final result
if result:
    print("Final result generated: PASS")
else:
    print("Final result generated: FAIL")

# Check expected content
expected_sections = [
    "Research completed",
    "Analysis completed",
    "Verification completed",
]

for section in expected_sections:
    if section in result:
        print(f"{section}: PASS")
    else:
        print(f"{section}: FAIL")

print("\n========== TEST COMPLETE ==========")