class Memory:
    """
    Stores task results and execution history.
    """

    def __init__(self):
        self.task_results = {}
        self.execution_history = []

    def store_result(self, task_id: str, result: str):
        """
        Store the result of a completed task.
        """

        self.task_results[task_id] = result
        self.execution_history.append(task_id)

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