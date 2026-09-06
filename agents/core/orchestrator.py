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

                self.task_manager.tasks[subtask.id] = subtask

                # Check dependencies
                dependencies_ready = all(
                    self.task_manager.tasks.get(dep_id)
                    and self.task_manager.tasks[dep_id].status
                    == TaskStatus.COMPLETED
                    for dep_id in subtask.dependencies
                )

                if not dependencies_ready:
                    continue

                # Find the required agent
                capability = self._detect_capability(subtask)

                agent = self.agent_registry.get(capability)

                # No agent available
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

                # -------------------------------------------------
                # Retry agent execution
                # -------------------------------------------------

                max_retries = 2
                attempt = 0
                result = None
                execution_successful = False

                while attempt <= max_retries:

                    print(
                        f"Attempt {attempt + 1} "
                        f"of {max_retries + 1}"
                    )

                    try:
                        result = agent.execute(subtask)
                        execution_successful = True

                        print(
                            f"Attempt {attempt + 1} "
                            f"succeeded."
                        )

                        break

                    except Exception as error:

                        attempt += 1

                        print(
                            f"Attempt failed: {error}"
                        )

                        if attempt > max_retries:

                            subtask.status = TaskStatus.FAILED

                            subtask.error = (
                                f"Agent failed after "
                                f"{max_retries + 1} attempts: "
                                f"{error}"
                            )

                            print(
                                f"Failed: {subtask.id} "
                                f"after "
                                f"{max_retries + 1} attempts"
                            )

                # -------------------------------------------------
                # Handle execution result
                # -------------------------------------------------

                if execution_successful:

                    subtask.result = result
                    subtask.status = TaskStatus.COMPLETED

                    results.append(result)

                    print(
                        f"Completed: {subtask.id}"
                    )

                pending.remove(subtask)
                progress = True

            # -------------------------------------------------
            # Detect unresolved dependencies
            # -------------------------------------------------

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
                    f"Failed: {subtask.id} - "
                    f"{subtask.error}"
                )

            task.status = TaskStatus.FAILED

            task.error = (
                "One or more subtasks failed."
            )

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

        final_result = (
            self.synthesis_agent.synthesize(results)
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