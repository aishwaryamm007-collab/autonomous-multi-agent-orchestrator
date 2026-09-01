from agents.core.models import Task, TaskStatus
from agents.core.task_manager import TaskManager
from agents.core.llm_service import LLMService
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
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.verification_agent = VerificationAgent()
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

        # Step 1: Planning
        print("\n[1] Planning...")
        subtasks = self.planner.plan(task)

        results = []

        # Step 2: Execute subtasks
        print("\n[2] Executing subtasks...")

        for subtask in subtasks:
            self.task_manager.tasks[subtask.id] = subtask

            if "research" in subtask.id:
                result = self.research_agent.execute(subtask)

            elif "analysis" in subtask.id:
                result = self.analysis_agent.execute(subtask)

            elif "verification" in subtask.id:
                result = self.verification_agent.execute(subtask)

            else:
                result = f"No agent available for: {subtask.goal}"

            subtask.result = result
            subtask.status = TaskStatus.COMPLETED

            results.append(result)

        # Step 3: Synthesis
        print("\n[3] Synthesizing results...")

        final_result = self.synthesis_agent.synthesize(results)

        task.result = final_result

        self.task_manager.update_status(
            task.id,
            TaskStatus.COMPLETED,
        )

        print("\n========== ORCHESTRATOR COMPLETE ==========")

        return final_result