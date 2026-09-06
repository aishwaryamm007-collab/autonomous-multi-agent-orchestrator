from agents.core.models import Task
from agents.core.orchestrator import Orchestrator


# -------------------------------------------------
# TEST 1: Successful workflow
# -------------------------------------------------

print("\n========== TEST 1: SUCCESSFUL WORKFLOW ==========")

task = Task(
    id="workflow-001",
    goal="Research Python and Java",
)

orchestrator = Orchestrator()

final_result = orchestrator.execute(task)

print("\n========== FINAL OUTPUT ==========")
print(final_result)
print("==================================")


# -------------------------------------------------
# TEST 2: Failure handling
# -------------------------------------------------

print("\n========== TEST 2: FAILURE HANDLING ==========")

failure_task = Task(
    id="workflow-002",
    goal="Research Python and Java",
)

failure_orchestrator = Orchestrator()

# Force the registry to return no agent.
# This simulates an unavailable agent.
failure_orchestrator.agent_registry.get = (
    lambda capability: None
)

failure_result = failure_orchestrator.execute(
    failure_task
)

print("\n========== FAILURE OUTPUT ==========")
print(failure_result)
print("====================================")