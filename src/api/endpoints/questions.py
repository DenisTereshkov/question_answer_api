from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.schemas.question import QuestionCreate, Question
from src.models.question import Question as QuestionModel

router = APIRouter()


@router.post("/", response_model=Question)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):
    db_question = QuestionModel(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return Question(
        id=db_question.id,
        text=db_question.text,
        created_at=db_question.created_at
    )


@router.get("/{question_id}", response_model=Question)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    db_question = db.query(QuestionModel).filter(
        QuestionModel.id == question_id
    ).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return Question(
        id=db_question.id,
        text=db_question.text,
        created_at=db_question.created_at
    )
