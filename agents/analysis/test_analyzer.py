from agents.core.models import Task
from agents.analysis.analyzer import AnalysisAgent


task = Task(
    id="analysis-001",
    goal="Analyze Python research",
)

agent = AnalysisAgent()

result = agent.execute(task)

print("\nFinal result:")
print(result)
