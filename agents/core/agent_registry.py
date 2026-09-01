from typing import Callable


class AgentRegistry:
    """
    Registry for discovering and selecting agents.
    """

    def __init__(self):
        self._agents: dict[str, Callable] = {}

    def register(self, capability: str, agent: Callable) -> None:
        self._agents[capability] = agent

    def get(self, capability: str) -> Callable | None:
        return self._agents.get(capability)

    def capabilities(self) -> list[str]:
        return list(self._agents.keys())