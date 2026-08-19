from agents.core.models import Task, TaskStatus


class TaskManager:
    def __init__(self):
        self.tasks: dict[str, Task] = {}

    def create_task(self, task_id: str, goal: str) -> Task:
        task = Task(
            id=task_id,
            goal=goal,
        )

        self.tasks[task_id] = task
        return task

    def get_task(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)

    def update_status(
        self,
        task_id: str,
        status: TaskStatus,
    ) -> Task | None:
        task = self.tasks.get(task_id)

        if task is None:
            return None

        task.status = status
        return task