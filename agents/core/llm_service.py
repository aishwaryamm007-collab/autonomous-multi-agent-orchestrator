from agents.core.plan_schema import PlanResponse, PlannedSubtask


class LLMService:
    """
    Mock LLM service used for development and testing.

    Generates a structured task plan based on the user's goal
    without requiring an external API.
    """

    def generate(self, prompt: str) -> PlanResponse:
        """
        Generate a structured plan from the planner prompt.
        """

        print("\nLLM prompt received:")
        print(prompt)

        goal = self._extract_goal(prompt)

        print(f"\nDetected user goal: {goal}")

        subtasks = self._generate_plan(goal)

        return PlanResponse(subtasks=subtasks)

    def _extract_goal(self, prompt: str) -> str:
        """
        Extract only the user goal from the planner prompt.
        """

        marker = "User goal:"
        end_marker = "Return a structured list of subtasks."

        if marker in prompt:
            goal = prompt.split(marker, 1)[1]

            if end_marker in goal:
                goal = goal.split(end_marker, 1)[0]

            goal = goal.strip()

            if goal:
                return goal

        return prompt.strip()

    def _generate_plan(self, goal: str) -> list[PlannedSubtask]:
        """
        Generate subtasks based on the user's goal.
        """

        goal_lower = goal.lower()

        # ---------------------------------------------
        # Research-related goals
        # ---------------------------------------------
        if "research" in goal_lower:

            subtasks = []

            if "python" in goal_lower:
                subtasks.append(
                    PlannedSubtask(
                        id="research-python",
                        goal="Research Python",
                    )
                )

            if "java" in goal_lower:
                dependencies = []

                if any(
                    subtask.id == "research-python"
                    for subtask in subtasks
                ):
                    dependencies = ["research-python"]

                subtasks.append(
                    PlannedSubtask(
                        id="research-java",
                        goal="Research Java",
                        dependencies=dependencies,
                    )
                )

            if (
                "machine learning" in goal_lower
                or "ml" in goal_lower
            ):
                subtasks.append(
                    PlannedSubtask(
                        id="research-machine-learning",
                        goal="Research Machine Learning",
                    )
                )

            if (
                "artificial intelligence" in goal_lower
                or "ai" in goal_lower
            ):
                subtasks.append(
                    PlannedSubtask(
                        id="research-ai",
                        goal="Research Artificial Intelligence",
                    )
                )

            if subtasks:
                return subtasks

        # ---------------------------------------------
        # Analysis-related goals
        # ---------------------------------------------
        if "analy" in goal_lower:
            return [
                PlannedSubtask(
                    id="analysis-task",
                    goal=f"Analyze: {goal}",
                )
            ]

        # ---------------------------------------------
        # Verification-related goals
        # ---------------------------------------------
        if (
            "verif" in goal_lower
            or "validate" in goal_lower
        ):
            return [
                PlannedSubtask(
                    id="verification-task",
                    goal=f"Verify: {goal}",
                )
            ]

        # ---------------------------------------------
        # Development-related goals
        # ---------------------------------------------
        if (
            "build" in goal_lower
            or "develop" in goal_lower
            or "create" in goal_lower
        ):
            return [
                PlannedSubtask(
                    id="research-requirements",
                    goal=f"Research requirements for: {goal}",
                ),
                PlannedSubtask(
                    id="analyze-solution",
                    goal=f"Analyze solution for: {goal}",
                    dependencies=[
                        "research-requirements"
                    ],
                ),
                PlannedSubtask(
                    id="verify-solution",
                    goal=f"Verify solution for: {goal}",
                    dependencies=[
                        "analyze-solution"
                    ],
                ),
            ]

        # ---------------------------------------------
        # General fallback
        # ---------------------------------------------
        return [
            PlannedSubtask(
                id="general-task",
                goal=goal,
            )
        ]