import json
from pathlib import Path

from agents.core.models import Task


class Memory:
    """
    Stores task results, execution history, and complete task state.
    """

    def __init__(self, file_path: str = "memory.json"):
        self.file_path = Path(file_path)

        self.task_results = {}
        self.execution_history = []
        self.task_states = {}

        self.load()

    def store_result(self, task_id: str, result: str):
        """
        Store the result of a completed task.
        """

        self.task_results[task_id] = result

        if task_id not in self.execution_history:
            self.execution_history.append(task_id)

        self.save()

    def store_task(self, task: Task):
        """
        Store the complete state of a task.
        """

        self.task_states[task.id] = task.to_dict()

        if task.result is not None:
            self.task_results[task.id] = task.result

        if task.status.value == "completed":
            if task.id not in self.execution_history:
                self.execution_history.append(task.id)

        self.save()

    def get_result(self, task_id: str):
        """
        Retrieve a previously stored task result.
        """

        return self.task_results.get(task_id)

    def get_task(self, task_id: str):
        """
        Retrieve the stored state of a task.
        """

        return self.task_states.get(task_id)

    def get_all_results(self):
        """
        Return all stored task results.
        """

        return self.task_results.copy()

    def get_all_tasks(self):
        """
        Return all stored task states.
        """

        return self.task_states.copy()

    def get_history(self):
        """
        Return the order in which tasks were completed.
        """

        return self.execution_history.copy()

    def save(self):
        """
        Save memory to a JSON file.
        """

        data = {
            "task_results": self.task_results,
            "execution_history": self.execution_history,
            "task_states": self.task_states,
        }

        with open(
            self.file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                default=str,
            )

    def load(self):
        """
        Load memory from a JSON file if it exists.
        """

        if not self.file_path.exists():
            return

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        self.task_results = data.get(
            "task_results",
            {},
        )

        self.execution_history = data.get(
            "execution_history",
            [],
        )

        self.task_states = data.get(
            "task_states",
            {},
        )