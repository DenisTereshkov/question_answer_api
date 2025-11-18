from fastapi import APIRouter

from .endpoints import (
    questions_router,
)

main_router = APIRouter()

main_router.include_router(
    questions_router,
    prefix="/questions",
    tags=["Вопросы"],
)
