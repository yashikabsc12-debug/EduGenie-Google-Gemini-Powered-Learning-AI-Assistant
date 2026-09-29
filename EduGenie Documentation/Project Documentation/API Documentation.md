# EduGenie – API Documentation

## 1. API Overview

EduGenie provides REST API endpoints through the FastAPI backend.

## 2. Question and Answer API

### Endpoint

```text
POST /qa
Purpose

Provides AI-generated answers to user questions.

3. Explanation API
Endpoint
POST /explain
Purpose

Generates simplified explanations for educational topics.

4. Quiz API
Endpoint
POST /quiz
Purpose

Generates multiple-choice questions from educational content.

5. Summarization API
Endpoint
POST /summarize
Purpose

Generates concise summaries from educational text.

6. Learning Path API
Endpoint
POST /learn/recommendations
Purpose

Generates personalized learning recommendations based on the learner's topic, level, and learning goal.

7. API Request Flow
User Input
    ↓
Frontend
    ↓
FastAPI API Endpoint
    ↓
AI Processing
    ↓
Generated Response
    ↓
Frontend
    ↓
User
8. API Documentation Interface

FastAPI provides an interactive API documentation interface that can be used to view and test the available endpoints.