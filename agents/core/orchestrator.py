from agents.core.agent_registry import AgentRegistry
from agents.core.llm_service import LLMService
from agents.core.models import Task, TaskStatus
from agents.core.task_manager import TaskManager
from agents.planner.planner import PlannerAgent
from agents.research.researcher import ResearchAgent
from agents.analysis.analyzer import AnalysisAgent
from agents.verification.verifier import VerificationAgent
from agents.synthesis.synthesizer import SynthesisAgent


class Orchestrator:
    """
    Coordinates the execution of multiple specialized agents.
    """

    def __init__(self):
        self.task_manager = TaskManager()

        llm_service = LLMService()

        self.planner = PlannerAgent(llm_service)
        self.synthesis_agent = SynthesisAgent()

        self.agent_registry = AgentRegistry()

        self.agent_registry.register(
            "research",
            ResearchAgent(),
        )

        self.agent_registry.register(
            "analysis",
            AnalysisAgent(),
        )

        self.agent_registry.register(
            "verification",
            VerificationAgent(),
        )

    def execute(self, task: Task) -> str:
        """
        Execute a complete multi-agent workflow.
        """

        print("\n========== ORCHESTRATOR START ==========")

        self.task_manager.tasks[task.id] = task

        self.task_manager.update_status(
            task.id,
            TaskStatus.RUNNING,
        )

        print("\n[1] Planning...")

        subtasks = self.planner.plan(task)

        results = []

        print("\n[2] Executing subtasks...")

        for subtask in subtasks:
            self.task_manager.tasks[subtask.id] = subtask

            capability = self._detect_capability(subtask)

            agent = self.agent_registry.get(capability)

            if agent is None:
                subtask.status = TaskStatus.FAILED
                subtask.error = (
                    f"No agent found for capability: {capability}"
                )
                continue

            result = agent.execute(subtask)

            subtask.result = result
            subtask.status = TaskStatus.COMPLETED

            results.append(result)

        print("\n[3] Synthesizing results...")

        final_result = self.synthesis_agent.synthesize(results)

        task.result = final_result

        self.task_manager.update_status(
            task.id,
            TaskStatus.COMPLETED,
        )

        print("\n========== ORCHESTRATOR COMPLETE ==========")

        return final_result

    def _detect_capability(self, task: Task) -> str:
        """
        Determine which capability is required for a task.
        """

        task_text = f"{task.id} {task.goal}".lower()

        for capability in self.agent_registry.capabilities():
            if capability in task_text:
                return capability

        return "unknown"