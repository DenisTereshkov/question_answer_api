from fastapi import APIRouter

from .endpoints import answers_router, questions_router

main_router = APIRouter()

main_router.include_router(
    questions_router,
    prefix="/questions",
    tags=["Вопросы"],
)

main_router.include_router(
    answers_router,
    tags=["Ответы"],
)
