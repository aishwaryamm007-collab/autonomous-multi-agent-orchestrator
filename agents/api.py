from fastapi import FastAPI, HTTPException

from agents.core.models import TaskStatus
from agents.core.task_manager import TaskManager


app = FastAPI(
    title="Autonomous Multi-Agent Task Orchestrator",
    version="0.1.0",
)

task_manager = TaskManager()


@app.get("/")
def root():
    return {
        "message": "Autonomous Multi-Agent Task Orchestrator is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/tasks")
def create_task(task_id: str, goal: str):
    task = task_manager.create_task(task_id, goal)

    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = task_manager.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@app.patch("/tasks/{task_id}/status")
def update_task_status(
    task_id: str,
    status: TaskStatus,
):
    task = task_manager.update_status(task_id, status)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task