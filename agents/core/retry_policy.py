class RetryPolicy:
    """
    Controls how many times an agent execution can be retried.
    """

    def __init__(self, max_retries: int = 2):
        if max_retries < 0:
            raise ValueError(
                "max_retries cannot be negative"
            )

        self.max_retries = max_retries

    def total_attempts(self) -> int:
        """
        Return the maximum number of total attempts.
        """

        return self.max_retries + 1

    def should_retry(self, attempt: int) -> bool:
        """
        Determine whether another attempt should be made.

        attempt is the number of attempts already completed.
        """

        return attempt < self.total_attempts()