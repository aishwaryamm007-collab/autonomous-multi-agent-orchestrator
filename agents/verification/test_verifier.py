from agents.core.models import Task
from agents.verification.verifier import VerificationAgent


task = Task(
    id="verification-001",
    goal="Verify Python research",
)

agent = VerificationAgent()

result = agent.execute(task)

print("\nFinal result:")
print(result)