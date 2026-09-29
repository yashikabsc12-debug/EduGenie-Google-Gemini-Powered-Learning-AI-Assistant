# EduGenie – Integration Testing

## 1. Integration Testing Overview

Integration testing was performed to verify the communication between the frontend, FastAPI backend, and AI service.

## 2. Integration Flow

```text
User
  ↓
Frontend
  ↓
FastAPI Backend
  ↓
Gemini AI
  ↓
Generated Response
  ↓
FastAPI Backend
  ↓
Frontend
  ↓
User

3. Frontend and Backend Integration

The frontend form sends a POST request to the appropriate FastAPI endpoint.

The backend processes the request and returns the generated result to the frontend.

4. AI Integration

The backend connects the learning requests with the AI service to generate responses for the different learning features.

5. Result Display

The generated result is returned to the frontend and displayed to the user in real time.

6. Result

The integration testing verified the complete communication flow between the application components.