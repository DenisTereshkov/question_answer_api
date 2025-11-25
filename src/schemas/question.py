from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)


class Question(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    created_at: datetime


class QuestionWithAnswers(Question):
    answers: List['Answer'] = []


from .answer import Answer  # noqa

QuestionWithAnswers.model_rebuild()
