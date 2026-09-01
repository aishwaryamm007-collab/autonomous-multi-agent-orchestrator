from agents.core.models import Task


class ResearchAgent:
    """
    Agent responsible for executing research-related subtasks.
    """

    def __init__(self):
        pass

    def execute(self, task: Task) -> str:
        """
        Execute a research task and return the result.
        """

        print("\nResearch Agent received task:")
        print(f"Task ID: {task.id}")
        print(f"Goal: {task.goal}")

        result = f"Research completed for: {task.goal}"

        print("\nResearch result:")
        print(result)

        return result