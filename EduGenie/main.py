from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import APP_NAME
from models import (
    QARequest,
    ExplainRequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
)
from services.gemini_service import GeminiService, GeminiServiceError


app = FastAPI(
    title=APP_NAME,
    description="AI-powered learning assistant using Google Gemini.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

gemini_service = GeminiService()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": APP_NAME,
        },
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": APP_NAME,
    }


@app.get("/api")
async def api_info():
    return {
        "name": APP_NAME,
        "version": "1.0.0",
        "endpoints": [
            "POST /qa",
            "POST /explain",
            "POST /quiz",
            "POST /summarize",
            "POST /learn/recommendations",
        ],
    }


@app.post("/qa")
async def question_answer(request: QARequest):
    try:
        answer = gemini_service.answer_question(
            question=request.question,
            level=request.level,
        )

        return {
            "success": True,
            "answer": answer,
        }

    except GeminiServiceError as error:
        return {
            "success": False,
            "error": str(error),
        }


@app.post("/explain")
async def explain_topic(request: ExplainRequest):
    try:
        explanation = gemini_service.explain_topic(
            topic=request.topic,
            level=request.level,
        )

        return {
            "success": True,
            "explanation": explanation,
        }

    except GeminiServiceError as error:
        return {
            "success": False,
            "error": str(error),
        }


@app.post("/quiz")
async def generate_quiz(request: QuizRequest):
    try:
        quiz = gemini_service.generate_quiz(
            topic=request.topic,
            number_of_questions=request.number_of_questions,
            level=request.level,
        )

        return {
            "success": True,
            "quiz": quiz,
        }

    except GeminiServiceError as error:
        return {
            "success": False,
            "error": str(error),
        }


@app.post("/summarize")
async def summarize_text(request: SummaryRequest):
    try:
        summary = gemini_service.summarize_text(
            text=request.text,
            level=request.level,
        )

        return {
            "success": True,
            "summary": summary,
        }

    except GeminiServiceError as error:
        return {
            "success": False,
            "error": str(error),
        }


@app.post("/learn/recommendations")
async def learning_recommendations(request: LearningPathRequest):
    try:
        recommendations = gemini_service.create_learning_path(
            topic=request.topic,
            goal=request.goal,
            level=request.level,
        )

        return {
            "success": True,
            "recommendations": recommendations,
        }

    except GeminiServiceError as error:
        return {
            "success": False,
            "error": str(error),
        }
