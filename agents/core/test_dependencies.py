from agents.core.models import Task, TaskStatus
from agents.core.task_manager import TaskManager


print("\n========== DEPENDENCY TEST ==========")

manager = TaskManager()

task_a = Task(
    id="task-a",
    goal="First task",
)

task_b = Task(
    id="task-b",
    goal="Second task",
    dependencies=["task-a"],
)

task_c = Task(
    id="task-c",
    goal="Third task",
    dependencies=["task-b"],
)

manager.tasks[task_a.id] = task_a
manager.tasks[task_b.id] = task_b
manager.tasks[task_c.id] = task_c


# ---------------------------------------------
# Test 1: Task B should wait for Task A
# ---------------------------------------------

b_ready = all(
    manager.tasks.get(dep_id)
    and manager.tasks[dep_id].status == TaskStatus.COMPLETED
    for dep_id in task_b.dependencies
)

if not b_ready:
    print("Task B waits for Task A: PASS")
else:
    print("Task B waits for Task A: FAIL")


# ---------------------------------------------
# Complete Task A
# ---------------------------------------------

task_a.status = TaskStatus.COMPLETED


b_ready = all(
    manager.tasks.get(dep_id)
    and manager.tasks[dep_id].status == TaskStatus.COMPLETED
    for dep_id in task_b.dependencies
)

if b_ready:
    print("Task B becomes ready after Task A: PASS")
else:
    print("Task B becomes ready after Task A: FAIL")


# ---------------------------------------------
# Test 2: Task C should still wait for B
# ---------------------------------------------

c_ready = all(
    manager.tasks.get(dep_id)
    and manager.tasks[dep_id].status == TaskStatus.COMPLETED
    for dep_id in task_c.dependencies
)

if not c_ready:
    print("Task C waits for Task B: PASS")
else:
    print("Task C waits for Task B: FAIL")


# ---------------------------------------------
# Complete Task B
# ---------------------------------------------

task_b.status = TaskStatus.COMPLETED


c_ready = all(
    manager.tasks.get(dep_id)
    and manager.tasks[dep_id].status == TaskStatus.COMPLETED
    for dep_id in task_c.dependencies
)

if c_ready:
    print("Task C becomes ready after Task B: PASS")
else:
    print("Task C becomes ready after Task B: FAIL")


print("========== TEST COMPLETE ==========")