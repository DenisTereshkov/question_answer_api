from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Answer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    user_id: int
    question_id: int
    created_at: datetime


class AnswerCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)
    user_id: str = Field(..., min_length=1, max_length=2000)
