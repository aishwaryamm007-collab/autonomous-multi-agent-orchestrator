from agents.core.models import Task


class AnalysisAgent:
    """
    Agent responsible for analyzing research-related subtasks.
    """

    def __init__(self):
        pass

    def execute(self, task: Task) -> str:
        """
        Analyze a task and return the analysis result.
        """

        print("\nAnalysis Agent received task:")
        print(f"Task ID: {task.id}")
        print(f"Goal: {task.goal}")

        result = f"Analysis completed for: {task.goal}"

        print("\nAnalysis result:")
        print(result)

        return result