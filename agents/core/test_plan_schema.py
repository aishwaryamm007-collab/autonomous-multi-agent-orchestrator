from agents.core.plan_schema import PlanResponse


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