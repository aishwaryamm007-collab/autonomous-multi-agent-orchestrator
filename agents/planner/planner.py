from agents.core.models import Task


class PlannerAgent:
    def plan(self, task: Task) -> list[Task]:
        subtasks = [
            Task(
                id=f"{task.id}-research",
                goal=f"Research the following goal: {task.goal}",
                parent_task_id=task.id,
            ),
            Task(
                id=f"{task.id}-analysis",
                goal=f"Analyze the research related to: {task.goal}",
                parent_task_id=task.id,
            ),
            Task(
                id=f"{task.id}-verification",
                goal=f"Verify the results for: {task.goal}",
                parent_task_id=task.id,
            ),
        ]

        task.subtasks = [subtask.id for subtask in subtasks]

        return subtasks