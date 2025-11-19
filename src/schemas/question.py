from datetime import datetime

from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Текст вопроса"
    )


class Question(BaseModel):
    id: int = Field(..., description="ID вопроса")
    text: str = Field(..., description="Текст вопроса")
    created_at: datetime = Field(..., description="Дата создания")
