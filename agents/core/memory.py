import json
from pathlib import Path


class Memory:
    """
    Stores task results and execution history.
    """

    def __init__(self, file_path: str = "memory.json"):
        self.file_path = Path(file_path)

        self.task_results = {}
        self.execution_history = []

        self.load()

    def store_result(self, task_id: str, result: str):
        """
        Store the result of a completed task.
        """

        self.task_results[task_id] = result
        self.execution_history.append(task_id)

        self.save()

    def get_result(self, task_id: str):
        """
        Retrieve a previously stored task result.
        """

        return self.task_results.get(task_id)

    def get_all_results(self):
        """
        Return all stored task results.
        """

        return self.task_results.copy()

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
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self):
        """
        Load memory from a JSON file if it exists.
        """

        if not self.file_path.exists():
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.task_results = data.get(
            "task_results",
            {},
        )

        self.execution_history = data.get(
            "execution_history",
            [],
        )