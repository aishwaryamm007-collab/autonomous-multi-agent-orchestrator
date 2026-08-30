from pydantic import BaseModel, Field


class PlannedSubtask(BaseModel):
    id: str = Field(min_length=1)
    goal: str = Field(min_length=1)


class PlanResponse(BaseModel):
    subtasks: list[PlannedSubtask]