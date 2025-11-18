from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QuestionCreate(BaseModel):
    text: str

class Question(BaseModel):
    id: int
    text: str  
    created_at: datetime
