from agents.core.memory import Memory


print("\n========== MEMORY TEST ==========")

memory = Memory()

# Store results
memory.store_result(
    "task-001",
    "Research completed successfully."
)

memory.store_result(
    "task-002",
    "Analysis completed successfully."
)

# Test retrieving a result
result = memory.get_result("task-001")

if result == "Research completed successfully.":
    print("Result retrieval: PASS")
else:
    print("Result retrieval: FAIL")

# Test all results
all_results = memory.get_all_results()

if len(all_results) == 2:
    print("Store multiple results: PASS")
else:
    print("Store multiple results: FAIL")

# Test execution history
history = memory.get_history()

if history == ["task-001", "task-002"]:
    print("Execution history: PASS")
else:
    print("Execution history: FAIL")

# Test unknown task
unknown_result = memory.get_result("unknown-task")

if unknown_result is None:
    print("Unknown task handling: PASS")
else:
    print("Unknown task handling: FAIL")

print("\n========== TEST COMPLETE ==========")