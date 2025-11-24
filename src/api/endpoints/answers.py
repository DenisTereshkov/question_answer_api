from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.schemas.answer import AnswerCreate, Answer
from src.models.answer import Answer as AnswerModel
from src.models.question import Question as QuestionModel

router = APIRouter()


@router.post("/questions/{question_id}/answers", response_model=Answer)
def create_answer(
    question_id: int,
    answer: AnswerCreate,
    db: Session = Depends(get_db),
):
    try:
        question_stmt = select(QuestionModel).where(QuestionModel.id == question_id)
        question =db.scalar(question_stmt)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        db_answer = AnswerModel(
            text=answer.text,
            user_id=answer.user_id,
            question_id=question_id,
        )
        db.add(db_answer)
        db.commit()
        db.refresh(db_answer)
        return db_answer
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid data")
    except SQLAlchemyError:

        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/questions/{question_id}/answers", response_model=list[Answer])
def get_answers(
    question_id: int,
    db: Session = Depends(get_db),
):
    try:
        answer_stmt = select(AnswerModel).where(AnswerModel.question_id == question_id)
        answers = db.scalars(answer_stmt).all()
        return answers
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")


@router.get("/questions/{question_id}/answers/{answer_id}", response_model=Answer)
def get_answer(
    question_id: int,
    answer_id: int,
    db: Session = Depends(get_db),
):
    try:
        answer_stmt = select(AnswerModel).where(
            AnswerModel.question_id == question_id,
            AnswerModel.id == answer_id,
        )
        answer = db.scalar(answer_stmt)
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found")
        return answer
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")


@router.delete("/questions/{question_id}/answers/{answer_id}")
def delete_answer(
    question_id: int,
    answer_id: int,
    db: Session = Depends(get_db),
):
    try:
        answer_stmt = select(AnswerModel).where(
            AnswerModel.question_id == question_id,
            AnswerModel.id == answer_id,
        )
        answer = db.scalar(answer_stmt)
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found")
        db.delete(answer)
        db.commit()
        return {"message": "Answer deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
