from agents.core.models import Task, TaskStatus


print("\n========== TASK SERIALIZATION TEST ==========")

task = Task(
    id="serialization-001",
    goal="Test persistent task state",
)

task.status = TaskStatus.COMPLETED
task.result = "Task completed successfully."
task.error = None
task.attempts = 2

data = task.to_dict()

print("\nSerialized task:")
print(data)

# Test basic fields
if data["id"] == "serialization-001":
    print("Task ID: PASS")
else:
    print("Task ID: FAIL")

if data["goal"] == "Test persistent task state":
    print("Task goal: PASS")
else:
    print("Task goal: FAIL")

# Test status
if data["status"] == TaskStatus.COMPLETED.value:
    print("Task status: PASS")
else:
    print("Task status: FAIL")

# Test result
if data["result"] == "Task completed successfully.":
    print("Task result: PASS")
else:
    print("Task result: FAIL")

# Test attempts
if data["attempts"] == 2:
    print("Task attempts: PASS")
else:
    print("Task attempts: FAIL")

print("\n========== TEST COMPLETE ==========")