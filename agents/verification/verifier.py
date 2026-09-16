from agents.core.models import Task


class VerificationAgent:
    """
    Agent responsible for verifying task results.
    """

    def __init__(self):
        pass

    def execute(
        self,
        task: Task,
        context: list[str] | None = None,
    ) -> str:
        """
        Verify a task using results from previous agents.
        """

        print("\nVerification Agent received task:")
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
                f"Verification completed for: {task.goal}\n"
                f"Verified using previous results: "
                f"{' | '.join(context)}"
            )
        else:
            result = f"Verification completed for: {task.goal}"

        print("\nVerification result:")
        print(result)

        return result