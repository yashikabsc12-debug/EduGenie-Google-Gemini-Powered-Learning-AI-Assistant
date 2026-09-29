# EduGenie – System Architecture

## 1. Overview

EduGenie follows a web-based AI application architecture consisting of a frontend interface, FastAPI backend, and Google Gemini AI service.

The architecture allows users to submit learning requests through the web interface. The FastAPI backend receives and processes the request and communicates with Google Gemini to generate the required educational response.

## 2. Main Components

The major components of the system are:

### 2.1 User

The user interacts with the EduGenie application through the web interface.

### 2.2 Frontend

The frontend provides the user interface for selecting a task, entering content, submitting requests, and viewing generated responses.

Technologies used include:

- HTML
- CSS
- JavaScript
- Jinja2

### 2.3 FastAPI Backend

FastAPI acts as the backend framework and provides REST API endpoints for the major EduGenie functionalities.

### 2.4 Google Gemini

Google Gemini provides the generative AI capabilities required for processing learning requests and generating responses.

### 2.5 Response

The generated response is returned from the backend and displayed through the frontend interface.

## 3. Architecture Flow

User
↓
Frontend Interface
↓
FastAPI Backend
↓
Google Gemini
↓
Generated Response
↓
FastAPI Backend
↓
Frontend Interface
↓
User

## 4. Functional Components

The major functional components are:

- Question and Answer
- Topic Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path

## 5. API Layer

The backend provides separate endpoints for the major functions:

- POST /qa
- POST /explain
- POST /quiz
- POST /summarize
- POST /learn/recommendations

## 6. Security Consideration

The Gemini API key is stored on the backend through environment variables and is not exposed directly to the frontend.

## 7. Design Objective

The architecture is designed to keep the user interface, backend processing, and AI service interaction organized into separate components.