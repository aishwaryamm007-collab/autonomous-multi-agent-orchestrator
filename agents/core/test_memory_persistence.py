from pathlib import Path

from agents.core.memory import Memory


print("\n========== MEMORY PERSISTENCE TEST ==========")

file_path = "test_memory.json"
Path(file_path).unlink(missing_ok=True)


# ---------------------------------------------
# Step 1: Create memory and store data
# ---------------------------------------------

memory = Memory(file_path)

memory.store_result(
    "task-001",
    "Research completed successfully.",
)

memory.store_result(
    "task-002",
    "Analysis completed successfully.",
)

memory.save()

print("Memory saved: PASS")


# ---------------------------------------------
# Step 2: Create a new Memory object
# ---------------------------------------------

new_memory = Memory(file_path)

new_memory.load()

print("Memory loaded successfully.")


# ---------------------------------------------
# Step 3: Verify stored results
# ---------------------------------------------

result = new_memory.get_result("task-001")

if result == "Research completed successfully.":
    print("Result persistence: PASS")
else:
    print("Result persistence: FAIL")


# ---------------------------------------------
# Step 4: Verify execution history
# ---------------------------------------------

history = new_memory.get_history()

if history == ["task-001", "task-002"]:
    print("History persistence: PASS")
else:
    print("History persistence: FAIL")


print("\nStored results:")

for task_id, task_result in new_memory.get_all_results().items():
    print(f"- {task_id}: {task_result}")


print("\n========== TEST COMPLETE ==========")
