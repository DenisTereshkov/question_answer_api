from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.models.question import Question as QuestionModel
from src.schemas.question import Question, QuestionCreate, QuestionWithAnswers

router = APIRouter()


@router.post("/", response_model=Question)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):
    try:
        db_question = QuestionModel(text=question.text)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Question creation failed")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")


@router.get("/{question_id}", response_model=QuestionWithAnswers)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    try:
        from sqlalchemy.orm import joinedload
        stmt = (
            select(QuestionModel)
            .where(QuestionModel.id == question_id)
            .options(joinedload(QuestionModel.answers))
        )
        question = db.scalar(stmt)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Конвертируем в схему с ответами
        return QuestionWithAnswers.model_validate(question)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/", response_model=list[Question])
def get_all_questions(db: Session = Depends(get_db)):
    try:
        stmt = select(QuestionModel).order_by(QuestionModel.created_at.desc())
        questions = db.scalars(stmt).all()
        return questions
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")


@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    try:
        stmt = select(QuestionModel).where(QuestionModel.id == question_id)
        db_question = db.scalar(stmt)
        if not db_question:
            raise HTTPException(
                status_code=404, detail="Вопрос не найден"
            )
        db.delete(db_question)
        db.commit()
        return {"message": "Вопрос удален успешно"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
