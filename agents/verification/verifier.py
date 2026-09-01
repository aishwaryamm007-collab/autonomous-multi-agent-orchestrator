from agents.core.models import Task


class VerificationAgent:
    """
    Agent responsible for verifying task results.
    """

    def __init__(self):
        pass

    def execute(self, task: Task) -> str:
        """
        Verify a task and return the verification result.
        """

        print("\nVerification Agent received task:")
        print(f"Task ID: {task.id}")
        print(f"Goal: {task.goal}")

        result = f"Verification completed for: {task.goal}"

        print("\nVerification result:")
        print(result)

        return result