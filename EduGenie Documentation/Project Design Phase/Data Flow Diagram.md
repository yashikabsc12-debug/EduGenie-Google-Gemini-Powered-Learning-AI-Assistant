# EduGenie – Data Flow Diagram

## 1. Overview

The Data Flow Diagram (DFD) describes how data moves through the EduGenie system from the user to the application, backend, Google Gemini AI service, and back to the user.

## 2. Overall Data Flow

```text
User
  ↓
EduGenie Web Interface
  ↓
FastAPI Backend
  ↓
Google Gemini AI
  ↓
Generated Response
  ↓
FastAPI Backend
  ↓
EduGenie Web Interface
  ↓
User

## Feature-wise Data Flow

### Question and Answer

```text
User Question
     ↓
EduGenie Frontend
     ↓
/qa
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Generated Answer
     ↓
Frontend
     ↓
User

User Question
     ↓
EduGenie Frontend
     ↓
/qa
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Generated Answer
     ↓
Frontend
     ↓
User

Topic + Learning Level
     ↓
EduGenie Frontend
     ↓
/explain
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Generated Explanation
     ↓
Frontend
     ↓
User

Topic / Educational Content
     ↓
EduGenie Frontend
     ↓
/quiz
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Generated Quiz
     ↓
Frontend
     ↓
User

Educational Text
     ↓
EduGenie Frontend
     ↓
/summarize
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Generated Summary
     ↓
Frontend
     ↓
User

Topic + Learning Level + Learning Goal
     ↓
EduGenie Frontend
     ↓
/learn/recommendations
     ↓
FastAPI Backend
     ↓
Google Gemini
     ↓
Learning Recommendations
     ↓
Frontend
     ↓
User

