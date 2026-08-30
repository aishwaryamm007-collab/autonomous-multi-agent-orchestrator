from agents.core.plan_schema import PlanResponse


class LLMService:
    def generate(self, prompt: str) -> PlanResponse:
        """
        Temporary mock LLM response.

        The real OpenAI integration will replace this later.
        """

        return PlanResponse(
            subtasks=[
                {
                    "id": "research",
                    "goal": "Research the topic",
                },
                {
                    "id": "analysis",
                    "goal": "Analyze the research",
                },
                {
                    "id": "verification",
                    "goal": "Verify the results",
                },
            ]
        )