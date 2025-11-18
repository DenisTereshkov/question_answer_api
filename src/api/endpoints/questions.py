from datetime import datetime

from fastapi import APIRouter

from src.sсhemas.question import QuestionCreate, Question


router = APIRouter()


@router.post("/", response_model=Question)
def create_question(question: QuestionCreate):
    return Question(
        id=1,
        text=question.text,
        created_at=datetime.now()
    )
