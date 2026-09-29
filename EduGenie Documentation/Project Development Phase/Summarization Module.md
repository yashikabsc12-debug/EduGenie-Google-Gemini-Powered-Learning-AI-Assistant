# EduGenie – Summarization Module

## 1. Module Overview

The Summarization module helps students convert long educational passages into concise and easy-to-understand summaries.

## 2. AI Processing

The module uses Gemini's generative capabilities to process long paragraphs.

The main information is retained while unnecessary repetition is reduced. :contentReference[oaicite:0]{index=0}

## 3. Working Process

1. The user enters educational text.
2. The text is sent to the FastAPI backend.
3. The `/summarize` endpoint receives the request.
4. The Summarization module processes the content.
5. Gemini generates a concise summary.
6. The generated summary is returned to the frontend.
7. The summary is displayed to the user.

## 4. API Endpoint

```text
POST /summarize