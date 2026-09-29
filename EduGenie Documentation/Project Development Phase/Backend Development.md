# EduGenie – Backend Development

## 1. Backend Overview

The backend of EduGenie was developed using the FastAPI framework.

The backend is responsible for receiving user requests from the frontend, processing the requests, connecting with the AI modules, and returning the generated responses to the user.

## 2. FastAPI Backend

FastAPI was used to create the backend REST API for the EduGenie application.

The backend provides separate API endpoints for the major features of the system.

## 3. API Endpoints

The following endpoints were implemented:

- `/qa` – Question and Answer
- `/explain` – Topic Explanation
- `/quiz` – Quiz Generation
- `/summarize` – Text Summarization
- `/learn/recommendations` – Personalized Learning Recommendations

Each endpoint is connected to the corresponding module logic. :contentReference[oaicite:0]{index=0}

## 4. Request Processing

The backend follows the following process:

1. The user selects a learning task from the frontend.
2. The frontend sends the user's input to the FastAPI backend.
3. The appropriate API endpoint receives the request.
4. The request is processed by the corresponding AI module.
5. The generated result is returned by the backend.
6. The frontend displays the result to the user.

## 5. Module Integration

The FastAPI backend was connected with the major EduGenie modules:

- Question and Answer
- Topic Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path

This allows the different learning features to work through a single backend application. :contentReference[oaicite:1]{index=1}

## 6. Quiz Response

The quiz module generates multiple-choice questions with four options.

The generated quiz is returned in a structured format so that it can be displayed properly by the frontend. :contentReference[oaicite:2]{index=2}

## 7. Backend Testing

The backend was tested by sending requests to the different API endpoints and checking whether the expected responses were generated.

The main learning functions were tested using questions, topics, educational text, quiz requests, and learning-path requests. :contentReference[oaicite:3]{index=3}

## 8. Backend Development Result

The completed FastAPI backend provides the API layer required for EduGenie and connects the frontend with the AI-powered learning features.