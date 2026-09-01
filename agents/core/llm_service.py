from agents.core.plan_schema import PlanResponse, PlannedSubtask


class LLMService:
    """
    Mock LLM service used for development and testing.

    This returns structured planner output without requiring
    an external API.
    """

    def generate(self, prompt: str) -> PlanResponse:
        print("\nLLM prompt received:")
        print(prompt)

        return PlanResponse(
            subtasks=[
                PlannedSubtask(
                    id="research-python",
                    goal="Research Python",
                ),
                PlannedSubtask(
                    id="research-java",
                    goal="Research Java",
                    dependencies=["research-python"],
                ),
            ]
        )