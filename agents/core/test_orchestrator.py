from agents.core.models import Task
from agents.core.orchestrator import Orchestrator



# -------------------------------------------------
# TEST AGENT FOR RETRY HANDLING
# -------------------------------------------------

class FlakyAgent:
    def __init__(self):
        self.attempts = 0

    def execute(self, task):
        self.attempts += 1

        print(
            f"FlakyAgent attempt {self.attempts}"
        )

        if self.attempts < 3:
            raise Exception(
                "Temporary agent failure"
            )

        return (
            f"Success after {self.attempts} attempts"
        )


# -------------------------------------------------
# TEST 1: SUCCESSFUL WORKFLOW
# -------------------------------------------------

print(
    "\n========== TEST 1: SUCCESSFUL WORKFLOW =========="
)

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
# TEST 2: FAILURE HANDLING
# -------------------------------------------------

print(
    "\n========== TEST 2: FAILURE HANDLING =========="
)

failure_task = Task(
    id="workflow-002",
    goal="Research Python and Java",
)

failure_orchestrator = Orchestrator()

# Simulate an unavailable agent
failure_orchestrator.agent_registry.get = (
    lambda capability: None
)

failure_result = failure_orchestrator.execute(
    failure_task
)

print("\n========== FAILURE OUTPUT ==========")
print(failure_result)
print("====================================")


# -------------------------------------------------
# TEST 3: RETRY HANDLING
# -------------------------------------------------

print(
    "\n========== TEST 3: RETRY HANDLING =========="
)

retry_task = Task(
    id="workflow-003",
    goal="Research Python",
)

retry_orchestrator = Orchestrator(max_retries=1)

flaky_agent = FlakyAgent()

# Make the planner return exactly one subtask.
retry_orchestrator.planner.plan = (
    lambda task: [
        Task(
            id="retry-research-python",
            goal="Research Python",
        )
    ]
)

# Replace the registry lookup with our
# controlled failing agent.
retry_orchestrator.agent_registry.get = (
    lambda capability: flaky_agent
)

retry_result = retry_orchestrator.execute(
    retry_task
)

print("\n========== RETRY OUTPUT ==========")
print(retry_result)
print("==================================")