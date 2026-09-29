from typing import Literal

from pydantic import BaseModel, Field


Level = Literal["beginner", "intermediate", "advanced"]


class QARequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=5000)
    level: Level = "beginner"


class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=5000)
    level: Level = "beginner"


class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=5000)
    number_of_questions: int = Field(default=5, ge=1, le=10)
    level: Level = "beginner"


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=15000)
    level: Level = "beginner"


class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=5000)
    goal: str = Field(..., min_length=1, max_length=3000)
    level: Level = "beginner"


class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str
    explanation: str


class QuizResponse(BaseModel):
    questions: list[QuizQuestion]
