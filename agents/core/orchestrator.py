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

                # Store the subtask
                self.task_manager.tasks[subtask.id] = subtask

                # Check whether all dependencies are completed
                dependencies_ready = all(
                    self.task_manager.tasks.get(dep_id)
                    and self.task_manager.tasks[dep_id].status
                    == TaskStatus.COMPLETED
                    for dep_id in subtask.dependencies
                )

                # Wait if dependencies are not ready
                if not dependencies_ready:
                    continue

                # Detect required capability
                capability = self._detect_capability(subtask)

                # Get the appropriate agent
                agent = self.agent_registry.get(capability)

                # Handle missing agent
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

                # Execute the agent
                result = agent.execute(subtask)

                # Store result
                subtask.result = result
                subtask.status = TaskStatus.COMPLETED

                results.append(result)

                print(f"Completed: {subtask.id}")

                # Remove completed task
                pending.remove(subtask)

                progress = True

            # If nothing could execute, dependencies
            # cannot be resolved.
            if not progress:
                for subtask in pending:
                    subtask.status = TaskStatus.FAILED
                    subtask.error = (
                        "Unresolved task dependencies"
                    )

                break

        # -------------------------------------------------
        # 3. HANDLE FAILURES
        # -------------------------------------------------

        failed_subtasks = [
            subtask
            for subtask in subtasks
            if subtask.status == TaskStatus.FAILED
        ]

        if failed_subtasks:
            print("\n[3] Some subtasks failed.")

            for subtask in failed_subtasks:
                print(
                    f"Failed: {subtask.id} - {subtask.error}"
                )

            task.status = TaskStatus.FAILED
            task.error = "One or more subtasks failed."

            self.task_manager.update_status(
                task.id,
                TaskStatus.FAILED,
            )

            return (
                "Orchestrator failed because "
                "one or more subtasks failed."
            )

        # -------------------------------------------------
        # 4. SYNTHESIZE RESULTS
        # -------------------------------------------------

        print("\n[4] Synthesizing results...")

        final_result = self.synthesis_agent.synthesize(
            results
        )

        task.result = final_result

        self.task_manager.update_status(
            task.id,
            TaskStatus.COMPLETED,
        )

        print(
            "\n========== ORCHESTRATOR COMPLETE =========="
        )

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