from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)


class Question(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    created_at: datetime
