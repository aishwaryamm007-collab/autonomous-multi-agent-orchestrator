from agents.core.models import Task, TaskStatus


task = Task(
    id="task-001",
    goal="Research Python and Java",
)

print(task)
print("Status:", task.status)
print("Status value:", task.status.value)
