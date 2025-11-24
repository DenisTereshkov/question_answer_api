from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

from src.core.db import Base


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1000), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    answers = relationship("Answer", back_populates="question", cascade="all, delete_orphan")
