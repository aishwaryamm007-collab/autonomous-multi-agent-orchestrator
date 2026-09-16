from agents.core.models import Task


class AnalysisAgent:
    """
    Agent responsible for analyzing research-related subtasks.
    """

    def __init__(self):
        pass

    def execute(
        self,
        task: Task,
        context: list[str] | None = None,
    ) -> str:
        """
        Analyze a task using results from previous agents.
        """

        print("\nAnalysis Agent received task:")
        print(f"Task ID: {task.id}")
        print(f"Goal: {task.goal}")

        if context:
            print("\nPrevious agent results:")
            for previous_result in context:
                print(f"- {previous_result}")
        else:
            print("\nNo previous agent results.")

        if context:
            result = (
                f"Analysis completed for: {task.goal}\n"
                f"Based on previous results: "
                f"{' | '.join(context)}"
            )
        else:
            result = f"Analysis completed for: {task.goal}"

        print("\nAnalysis result:")
        print(result)

        return result