from agents.core.plan_schema import PlanResponse, PlannedSubtask


class LLMService:
    """
    Local mock LLM service used for development and testing.

    This version does not require an API key or internet connection.
    It generates structured execution plans based on the user's goal.
    """

    def generate(self, prompt: str) -> PlanResponse:
        print("\nLLM prompt received:")
        print(prompt)

        goal = self._extract_goal(prompt)

        print(f"\nDetected user goal: {goal}")

        return self._generate_plan(goal)

    def _extract_goal(self, prompt: str) -> str:
        marker = "User goal:"
        end_marker = "Create a practical execution plan."

        if marker in prompt:
            goal = prompt.split(marker, 1)[1]

            if end_marker in goal:
                goal = goal.split(end_marker, 1)[0]

            goal = goal.strip()

            if goal:
                return goal

        return prompt.strip()

    def _generate_plan(self, goal: str) -> PlanResponse:
        goal_lower = goal.lower()
        subtasks = []

        # -------------------------------------------------
        # Build / Development Tasks
        # -------------------------------------------------

        if any(
            keyword in goal_lower
            for keyword in [
                "build",
                "develop",
                "create",
                "implement",
                "design",
            ]
        ):
            return PlanResponse(
                subtasks=[
                    PlannedSubtask(
                        id="research-requirements",
                        goal=f"Research requirements for: {goal}",
                        dependencies=[],
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
            )

        # -------------------------------------------------
        # Research / Learning Tasks
        # -------------------------------------------------

        if any(
            keyword in goal_lower
            for keyword in [
                "research",
                "investigate",
                "study",
                "learn",
                "learning",
                "find information",
            ]
        ):
            if "python" in goal_lower:
                subtasks.append(
                    PlannedSubtask(
                        id="research-python",
                        goal="Research Python",
                        dependencies=[],
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

            if "machine learning" in goal_lower:
                subtasks.append(
                    PlannedSubtask(
                        id="research-machine-learning",
                        goal="Research Machine Learning",
                        dependencies=[],
                    )
                )

            if (
                "artificial intelligence" in goal_lower
                or " ai " in f" {goal_lower} "
            ):
                subtasks.append(
                    PlannedSubtask(
                        id="research-ai",
                        goal="Research Artificial Intelligence",
                        dependencies=[],
                    )
                )

            if subtasks:
                return PlanResponse(
                    subtasks=subtasks
                )

        # -------------------------------------------------
        # Analysis Tasks
        # -------------------------------------------------

        if any(
            keyword in goal_lower
            for keyword in [
                "analyze",
                "analysis",
                "analyse",
                "evaluate",
            ]
        ):
            return PlanResponse(
                subtasks=[
                    PlannedSubtask(
                        id="analysis-task",
                        goal=f"Analyze: {goal}",
                        dependencies=[],
                    )
                ]
            )

        # -------------------------------------------------
        # Verification Tasks
        # -------------------------------------------------

        if any(
            keyword in goal_lower
            for keyword in [
                "verify",
                "verification",
                "validate",
                "validation",
                "check",
            ]
        ):
            return PlanResponse(
                subtasks=[
                    PlannedSubtask(
                        id="verification-task",
                        goal=f"Verify: {goal}",
                        dependencies=[],
                    )
                ]
            )

        # -------------------------------------------------
        # General Task
        # -------------------------------------------------

        return PlanResponse(
            subtasks=[
                PlannedSubtask(
                    id="general-task",
                    goal=goal,
                    dependencies=[],
                )
            ]
        )