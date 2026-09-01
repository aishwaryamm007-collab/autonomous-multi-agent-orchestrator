from agents.core.plan_schema import PlanResponse, PlannedSubtask
plan = PlanResponse(
    subtasks=[
        {
            "id": "research-python",
            "goal": "Research Python",
        },
        {
            "id": "research-java",
            "goal": "Research Java",
        },
    ]
)

print("Plan created successfully:")
print(plan)

print("\nSubtasks:")

for subtask in plan.subtasks:
    print(f"- {subtask.id}: {subtask.goal}")
print("\nTesting dependencies:")

subtask = PlannedSubtask(
    id="analysis-001",
    goal="Analyze research results",
    dependencies=["research-001"],
)

print(subtask)
print("Dependencies:", subtask.dependencies)   