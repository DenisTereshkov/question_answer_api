from .questions import router as questions_router # noqa
from .answers import router as answers_router # noqa

__all__ = [
    "questions_router",
    "answers_router",
]