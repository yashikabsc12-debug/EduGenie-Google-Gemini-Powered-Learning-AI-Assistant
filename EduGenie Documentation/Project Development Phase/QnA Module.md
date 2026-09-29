# EduGenie – QnA Module

## 1. Module Overview

The Question and Answer module allows students to ask academic and general knowledge questions and receive AI-generated answers.

## 2. AI Model

The project documentation specifies Gemini 1.5 Pro for the Question and Answer functionality.

Gemini provides contextual understanding for answering questions across different educational topics. :contentReference[oaicite:1]{index=1}

## 3. Working Process

The QnA module follows these steps:

1. The user enters a question.
2. The question is sent to the FastAPI backend.
3. The `/qa` endpoint receives the request.
4. The request is processed using the QnA module.
5. Gemini generates the answer.
6. The generated answer is returned to the frontend.
7. The answer is displayed to the user.

## 4. API Endpoint

```text
POST /qa