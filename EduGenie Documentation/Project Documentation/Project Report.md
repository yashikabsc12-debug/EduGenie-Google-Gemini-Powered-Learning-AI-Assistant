# EduGenie – Project Report

## 1. Project Title

EduGenie – Google Gemini Powered Learning Assistant

## 2. Project Overview

EduGenie is an AI-powered educational assistant designed to help students with their learning activities.

The system provides AI-based assistance for Question and Answer, Topic Explanation, Quiz Generation, Text Summarization, and Personalized Learning Recommendations.

## 3. Problem Statement

Students often face difficulties in understanding complex topics, revising lengthy educational content, preparing questions, and creating a structured learning plan.

EduGenie addresses these challenges by providing AI-powered learning assistance through a simple web interface.

## 4. Objectives

- To provide AI-powered Question and Answer assistance.
- To simplify complex educational topics.
- To generate quizzes for learning and revision.
- To summarize lengthy educational content.
- To provide personalized learning recommendations.
- To provide a simple and user-friendly learning interface.

## 5. Technologies Used

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Google Gemini AI
- Pydantic
- Uvicorn

## 6. Major Features

### Question and Answer

Allows students to ask academic and general knowledge questions and receive AI-generated answers.

### Topic Explanation

Provides simplified explanations for complex topics based on the learner's level.

### Quiz Generation

Generates multiple-choice questions from educational content.

### Text Summarization

Converts lengthy educational content into concise summaries.

### Personalized Learning Path

Generates step-by-step learning recommendations based on the learner's topic, level, and learning goal.

## 7. System Architecture

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

8. API Endpoints
POST /qa
POST /explain
POST /quiz
POST /summarize
POST /learn/recommendations
9. Project Workflow
The user opens the EduGenie web application.
The user selects a learning feature.
The user enters the required information.
The frontend sends the request to the FastAPI backend.
The backend processes the request.
The request is sent to the Gemini AI service.
Gemini generates the required response.
The backend returns the response.
The frontend displays the result to the user.
10. Testing

The application was tested to verify:

Frontend loading
Backend availability
API endpoint responses
Question and Answer functionality
Explanation functionality
Quiz generation
Text summarization
Personalized learning recommendations
11. Security

The Gemini API key is stored using environment variables and is not exposed in the frontend code.

The API key should not be committed to the GitHub repository.

12. Conclusion

EduGenie provides an AI-powered learning environment that combines multiple educational assistance features into a single web application.

The system helps students understand topics, obtain answers, generate quizzes, summarize content, and receive personalized learning recommendations.