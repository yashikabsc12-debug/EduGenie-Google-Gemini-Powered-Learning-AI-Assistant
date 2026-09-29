# EduGenie – Learning Path Module

## 1. Module Overview

The Learning Path module generates personalized learning recommendations for students.

It creates a structured learning path based on the learner's topic and learning level.

## 2. AI Processing

The `get_learning_recommendations` function uses Google Gemini to generate a personalized learning path.

The generated path covers concepts from beginner to advanced levels and can include useful learning resources such as videos, articles, and books. :contentReference[oaicite:0]{index=0}

## 3. Personalization

The learning path is designed to adapt to the learner's level.

The recommendations are organized according to difficulty so that learners can progress step by step. :contentReference[oaicite:1]{index=1}

## 4. Working Process

1. The user enters a topic.
2. The user provides the learning level.
3. The user provides the learning goal.
4. The request is sent to the FastAPI backend.
5. The `/learn/recommendations` endpoint receives the request.
6. Gemini generates the learning recommendations.
7. The generated learning path is returned to the frontend.
8. The recommendations are displayed to the user.

## 5. API Endpoint

```text
POST /learn/recommendations