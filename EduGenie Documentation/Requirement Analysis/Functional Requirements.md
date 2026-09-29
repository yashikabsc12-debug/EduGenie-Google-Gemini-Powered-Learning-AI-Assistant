# EduGenie – Functional Requirements

## 1. Functional Requirements Overview

Functional requirements describe the main functions that EduGenie must provide to the users.

## 2. User Interaction

The system shall allow users to interact with the EduGenie web interface and select the required learning feature.

## 3. Question and Answer

The system shall allow users to enter questions and receive AI-generated answers.

## 4. Topic Explanation

The system shall allow users to enter a topic and receive a simplified explanation according to the learning level.

## 5. Quiz Generation

The system shall generate multiple-choice questions from the educational content provided by the user.

The quiz shall contain questions with multiple options and correct answers.

## 6. Text Summarization

The system shall allow users to enter lengthy educational content and generate a concise summary.

## 7. Personalized Learning Path

The system shall generate personalized learning recommendations based on:

- Topic
- Learning level
- Learning goal

The recommendations can guide the learner from beginner to advanced concepts.

## 8. Backend API

The system shall provide REST API endpoints for the major learning functions:

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`

## 9. AI Processing

The system shall process user requests using the integrated AI service and return the generated response through the backend.

## 10. Result Display

The system shall display the generated response on the web interface after processing the user's request.

## 11. Error Handling

The system shall handle invalid, incomplete, or unsuccessful requests and provide an appropriate error response.

## 12. Functional Requirement Summary

EduGenie shall provide AI-powered Question and Answer, Topic Explanation, Quiz Generation, Text Summarization, and Personalized Learning Recommendations through a web-based interface.