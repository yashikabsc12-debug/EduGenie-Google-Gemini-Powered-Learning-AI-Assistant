# EduGenie – Explanation Module

## 1. Module Overview

The Explanation module helps learners understand complex topics through simplified and readable explanations.

## 2. AI Model

EduGenie uses the LaMini-Flan-T5 model for the Explanation module.

The model is designed to provide concise and context-aware responses that break down complex topics into easily understandable language. :contentReference[oaicite:0]{index=0}

## 3. Working Process

1. The user enters a topic.
2. The user provides the required learning level.
3. The request is sent to the FastAPI backend.
4. The `/explain` endpoint receives the request.
5. The Explanation module processes the request.
6. The AI generates a simplified explanation.
7. The result is returned to the frontend.
8. The explanation is displayed to the user.

## 4. API Endpoint

```text
POST /explain