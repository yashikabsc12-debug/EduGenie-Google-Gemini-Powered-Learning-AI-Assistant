import os

from dotenv import load_dotenv


load_dotenv()


APP_NAME = "EduGenie - Google Gemini Powered Learning Assistant"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash",
)


def validate_configuration():
    if not GEMINI_API_KEY:
        raise ValueError(
            "Gemini API key is missing. "
            "Please add GEMINI_API_KEY to your .env file."
        )