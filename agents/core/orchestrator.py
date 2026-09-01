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

        self.llm_service = LLMService()
        self.planner = PlannerAgent(self.llm_service)

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

        self.synthesis_agent = SynthesisAgent()

    def execute(self, task: Task) -> str:
        """
        Execute a complete multi-agent workflow.
        """

        print("\n========== ORCHESTRATOR START ==========")

        # Store the main task
        self.task_manager.tasks[task.id] = task

        self.task_manager.update_status(
            task.id,
            TaskStatus.RUNNING,
        )

        # -------------------------------------------------
        # 1. PLAN
        # -------------------------------------------------

        print("\n[1] Planning subtasks...")

        subtasks = self.planner.plan(task)

        print("\nGenerated subtasks:")

        for subtask in subtasks:
            print(
                f"- {subtask.id}: {subtask.goal} "
                f"| dependencies: {subtask.dependencies}"
            )

        # -------------------------------------------------
        # 2. EXECUTE SUBTASKS
        # -------------------------------------------------

        print("\n[2] Executing subtasks...")

        pending = subtasks.copy()
        results = []

        while pending:
            progress = False

            for subtask in pending.copy():

                # Store subtask in task manager
                self.task_manager.tasks[subtask.id] = subtask

                # Check whether all dependencies are completed
                dependencies_ready = all(
                    self.task_manager.tasks.get(dep_id)
                    and self.task_manager.tasks[dep_id].status
                    == TaskStatus.COMPLETED
                    for dep_id in subtask.dependencies
                )

                # If dependencies are not ready,
                # wait for the next iteration.
                if not dependencies_ready:
                    continue

                # Determine which agent should execute
                # this subtask.
                capability = self._detect_capability(subtask)

                agent = self.agent_registry.get(capability)

                # If no suitable agent exists,
                # mark the task as failed.
                if agent is None:
                    subtask.status = TaskStatus.FAILED
                    subtask.error = (
                        f"No agent found for capability: {capability}"
                    )

                    pending.remove(subtask)
                    progress = True

                    continue

                print(f"\nExecuting: {subtask.id}")
                print(f"Goal: {subtask.goal}")
                print(
                    f"Dependencies: {subtask.dependencies}"
                )

                # Execute the specialized agent
                result = agent.execute(subtask)

                # Store result and status
                subtask.result = result
                subtask.status = TaskStatus.COMPLETED

                results.append(result)

                print(f"Completed: {subtask.id}")

                # Remove from pending tasks
                pending.remove(subtask)

                progress = True

            # If no task could be executed,
            # dependencies cannot be resolved.
            if not progress:
                for subtask in pending:
                    subtask.status = TaskStatus.FAILED
                    subtask.error = (
                        "Unresolved task dependencies"
                    )

                break

        # -------------------------------------------------
        # 3. SYNTHESIZE
        # -------------------------------------------------

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