from agents.core.models import Task
from agents.research.researcher import ResearchAgent


task = Task(
    id="research-001",
    goal="Research Python programming",
)

agent = ResearchAgent()

result = agent.execute(task)

print("\nFinal result:")
print(result)