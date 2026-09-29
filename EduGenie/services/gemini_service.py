import json
import re
from typing import Any

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiServiceError(Exception):
    """Custom exception for Gemini service errors."""


class GeminiService:

    def __init__(self):
        if not GEMINI_API_KEY:
            raise GeminiServiceError(
                "Gemini API key is missing. "
                "Please create a .env file and add GEMINI_API_KEY."
            )

        try:
            self.client = genai.Client(
                api_key=GEMINI_API_KEY
            )

            self.model_name = GEMINI_MODEL

        except Exception as error:
            raise GeminiServiceError(
                f"Unable to initialize Gemini client: {error}"
            )

    def _generate(
        self,
        prompt: str,
        json_mode: bool = False,
    ) -> str:

        try:

            config = types.GenerateContentConfig(
                temperature=0.4,
                max_output_tokens=3000,
                system_instruction=(
                    "You are EduGenie, an educational AI assistant. "
                    "Give accurate, student-friendly and clear answers. "
                    "Adapt explanations to the student's level. "
                    "Do not invent facts. "
                    "When information is uncertain, clearly say so."
                ),
            )

            if json_mode:
                config.response_mime_type = "application/json"

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=config,
            )

            if not response or not response.text:
                raise GeminiServiceError(
                    "Gemini returned an empty response."
                )

            return response.text.strip()

        except GeminiServiceError:
            raise

        except Exception as error:
            raise GeminiServiceError(
                f"Gemini API error: {error}"
            )

    # ---------------------------------------------------------
    # Q&A
    # ---------------------------------------------------------

    def answer_question(
        self,
        question: str,
        level: str = "beginner",
    ) -> str:

        prompt = f"""
You are helping a {level}-level student.

Answer the following question clearly:

QUESTION:
{question}

Requirements:

1. Give a direct answer first.
2. Explain the concept simply.
3. Use an example when useful.
4. Avoid unnecessary complexity.
5. If the question contains multiple parts, answer each part.
6. Do not invent information.
7. Keep the answer educational and concise.
"""

        return self._generate(prompt)

    # ---------------------------------------------------------
    # EXPLANATION
    # ---------------------------------------------------------

    def explain_topic(
        self,
        topic: str,
        level: str = "beginner",
    ) -> str:

        prompt = f"""
Explain the following topic to a {level}-level student.

TOPIC:
{topic}

Use this structure:

1. Definition
2. How it works
3. Simple example
4. Real-world analogy
5. Key points to remember
6. Short self-check question

Use simple language.

Avoid assuming advanced knowledge unless required.
"""

        return self._generate(prompt)

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    def summarize_text(
        self,
        text: str,
        level: str = "beginner",
    ) -> str:

        prompt = f"""
Summarize the following text for a {level}-level student.

TEXT:
{text}

Requirements:

- Start with a short overview.
- Extract the main ideas.
- Use bullet points where appropriate.
- Keep important technical terms.
- Remove unnecessary repetition.
- Do not add facts that are not supported by the text.
- Make the summary easy to revise for exams.
"""

        return self._generate(prompt)

    # ---------------------------------------------------------
    # LEARNING PATH
    # ---------------------------------------------------------

    def create_learning_path(
        self,
        topic: str,
        goal: str,
        level: str = "beginner",
    ) -> str:

        prompt = f"""
Create a personalized learning path for a {level}-level student.

TOPIC:
{topic}

STUDENT GOAL:
{goal}

Create a practical progression.

Use this structure:

Stage 1 - Foundation
- What to learn
- Why it matters
- Practice activity

Stage 2 - Core Concepts
- What to learn
- Why it matters
- Practice activity

Stage 3 - Applied Learning
- What to build or practice
- Suggested project

Stage 4 - Advanced Learning
- Topics to explore next

Stage 5 - Final Project
- Suggested project
- Expected skills

Also include:

Recommended learning order
Common mistakes to avoid
How to measure progress

Keep the plan realistic for the student's level.
"""

        return self._generate(prompt)

    # ---------------------------------------------------------
    # QUIZ
    # ---------------------------------------------------------

    def generate_quiz(
        self,
        topic: str,
        number_of_questions: int = 5,
        level: str = "beginner",
    ) -> dict[str, Any]:

        prompt = f"""
Create a multiple-choice quiz for a {level}-level student.

TOPIC:
{topic}

NUMBER OF QUESTIONS:
{number_of_questions}

Return ONLY valid JSON.

Use exactly this format:

{{
  "questions": [
    {{
      "question": "Question text",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "answer": "Correct option text",
      "explanation": "Short explanation"
    }}
  ]
}}

Rules:

1. Generate exactly {number_of_questions} questions.
2. Every question must have exactly four options.
3. There must be only one correct answer.
4. The answer field must exactly match one option.
5. Add a short explanation.
6. Questions should test understanding, not only memorization.
7. Return JSON only.
"""

        raw_response = self._generate(
            prompt,
            json_mode=True,
        )

        data = self._parse_json(raw_response)

        self._validate_quiz(
            data,
            number_of_questions,
        )

        return data

    # ---------------------------------------------------------
    # JSON PARSER
    # ---------------------------------------------------------

    def _parse_json(
        self,
        text: str,
    ) -> dict[str, Any]:

        cleaned = text.strip()

        # Remove markdown JSON fences if Gemini returns them.
        cleaned = re.sub(
            r"^```json\s*",
            "",
            cleaned,
            flags=re.IGNORECASE,
        )

        cleaned = re.sub(
            r"^```\s*",
            "",
            cleaned,
        )

        cleaned = re.sub(
            r"\s*```$",
            "",
            cleaned,
        )

        try:
            return json.loads(cleaned)

        except json.JSONDecodeError:

            # Try to extract the JSON object.
            start = cleaned.find("{")
            end = cleaned.rfind("}")

            if start != -1 and end != -1:

                possible_json = cleaned[start:end + 1]

                try:
                    return json.loads(possible_json)

                except json.JSONDecodeError:
                    pass

            raise GeminiServiceError(
                "Gemini returned invalid quiz JSON."
            )

    # ---------------------------------------------------------
    # QUIZ VALIDATION
    # ---------------------------------------------------------

    def _validate_quiz(
        self,
        data: dict[str, Any],
        expected_count: int,
    ):

        if "questions" not in data:
            raise GeminiServiceError(
                "Quiz response does not contain questions."
            )

        questions = data["questions"]

        if not isinstance(questions, list):
            raise GeminiServiceError(
                "Quiz questions must be a list."
            )

        if len(questions) != expected_count:
            raise GeminiServiceError(
                f"Expected {expected_count} questions, "
                f"but received {len(questions)}."
            )

        for question in questions:

            required_fields = [
                "question",
                "options",
                "answer",
                "explanation",
            ]

            for field in required_fields:

                if field not in question:
                    raise GeminiServiceError(
                        f"Quiz question is missing: {field}"
                    )

            if len(question["options"]) != 4:
                raise GeminiServiceError(
                    "Every quiz question must have exactly 4 options."
                )

            if question["answer"] not in question["options"]:
                raise GeminiServiceError(
                    "Quiz answer must match one of the options."
                )