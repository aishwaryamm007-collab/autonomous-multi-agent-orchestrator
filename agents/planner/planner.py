from agents.core.llm_service import LLMService
from agents.core.models import Task
from agents.core.plan_schema import PlannedSubtask


class PlannerAgent:
    """
    Agent responsible for creating an execution plan
    from a user's task.
    """

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def plan(self, task: Task) -> list[Task]:
        """
        Generate subtasks using the LLM service.
        """

        prompt = f"""
You are an autonomous task planning agent.

Your job is to break the user's goal into logical subtasks.

User goal:
{task.goal}

Create a practical execution plan.

Each subtask must contain:
- id: a unique short identifier
- goal: a clear description of the task
- dependencies: a list of subtask IDs that must be completed first

Rules:
1. Create only the subtasks necessary to accomplish the goal.
2. Use dependencies when one subtask requires the result of another.
3. Use an empty list when a subtask has no dependencies.
4. Return ONLY valid JSON.
5. Do not include markdown.
6. Do not include explanations outside the JSON.

Return exactly this structure:

{{
    "subtasks": [
        {{
            "id": "task-1",
            "goal": "First task",
            "dependencies": []
        }},
        {{
            "id": "task-2",
            "goal": "Second task",
            "dependencies": ["task-1"]
        }}
    ]
}}
"""

        plan = self.llm_service.generate(prompt)

        subtasks = []

        for planned_subtask in plan.subtasks:
            subtasks.append(
                Task(
                    id=f"{task.id}-{planned_subtask.id}",
                    goal=planned_subtask.goal,
                    parent_task_id=task.id,
                    dependencies=[
                        f"{task.id}-{dependency}"
                        for dependency in planned_subtask.dependencies
                    ],
                )
            )

        return subtasks