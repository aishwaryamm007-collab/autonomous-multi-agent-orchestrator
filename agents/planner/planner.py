from agents.core.llm_service import LLMService
from agents.core.models import Task


class PlannerAgent:
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def plan(self, task: Task) -> list[Task]:
        prompt = f"""
You are a task planning agent.

Break the following user goal into smaller,
clear and executable subtasks.

User goal:
{task.goal}

Return a structured list of subtasks.
"""

        plan = self.llm_service.generate(prompt)

        subtasks = []

        for planned_subtask in plan.subtasks:
            subtasks.append(
                Task(
                    id=f"{task.id}-{planned_subtask.id}",
                    goal=planned_subtask.goal,
                    parent_task_id=task.id,
                )
            )

        task.subtasks = [subtask.id for subtask in subtasks]

        return subtasks