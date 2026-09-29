# EduGenie – Gemini AI Integration

## 1. AI Integration Overview

Google Gemini AI was integrated into EduGenie to provide AI-powered educational assistance.

The Gemini API is used to process student inputs and generate educational responses for the different learning features.

## 2. Gemini API

The Google Gemini API was used to connect EduGenie with the Gemini AI model.

An API key is required to establish the connection between the application and the Gemini AI service.

The API key is stored securely using environment variables and is not exposed in the frontend code. :contentReference[oaicite:0]{index=0}

## 3. AI-Powered Features

Gemini AI is used for the major learning functions of EduGenie, including:

- Question and Answer
- Topic Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path

The project documentation describes Gemini-based processing for QnA, quiz generation, summarization, and learning-path generation. :contentReference[oaicite:1]{index=1}

## 4. AI Request Flow

The AI integration follows this process:

User Input
↓
Frontend
↓
FastAPI Backend
↓
Gemini AI Service
↓
AI Processing
↓
Generated Response
↓
FastAPI Backend
↓
Frontend
↓
User

## 5. Prompt-Based Processing

The user's input is combined with the appropriate instructions for the selected learning task.

The AI then generates a response according to the selected task, such as an answer, explanation, quiz, summary, or learning recommendation.

## 6. Quiz Generation

For quiz generation, the AI is instructed to create multiple-choice questions with four options.

The generated quiz is returned in a structured format for display in the application. :contentReference[oaicite:2]{index=2}

## 7. Personalized Learning Path

The AI can generate a personalized learning path based on the learner's topic, learning level, and learning goal.

The generated path can contain learning stages and recommended resources. :contentReference[oaicite:3]{index=3}

## 8. API Key Security

The Gemini API key must not be placed directly inside frontend files or committed to the Git repository.

Environment variables are used to keep the API key separate from the application source code. :contentReference[oaicite:4]{index=4}

## 9. Integration Result

The Gemini AI integration enables EduGenie to provide AI-powered learning assistance through its FastAPI backend and frontend interface.