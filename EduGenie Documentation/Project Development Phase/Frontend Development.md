# EduGenie – Frontend Development

## 1. Frontend Overview

The frontend of EduGenie was developed to provide a simple and user-friendly interface for students.

HTML, CSS, and JavaScript were used to create the frontend interface. :contentReference[oaicite:0]{index=0}

## 2. User Interface

The EduGenie interface allows users to select the required learning task and provide their input.

The main task options include:

- Explain
- QnA
- Quiz
- Summary
- Recommend Path

## 3. Input Section

The frontend contains an input area where the user can enter a question, topic, or educational content depending on the selected task.

A submit button is provided to send the user's request to the backend.

## 4. Backend Integration

The frontend was connected with the FastAPI backend.

When the user submits a request, the frontend sends the input to the appropriate FastAPI endpoint using a POST request.

The backend processes the request and returns the generated result to the frontend. :contentReference[oaicite:1]{index=1}

## 5. Result Display

The generated response is displayed on the frontend after receiving the response from the backend.

This allows users to interact with the AI learning assistant and view the generated educational content in real time. :contentReference[oaicite:2]{index=2}

## 6. Styling

CSS was used to style the EduGenie interface.

The interface was designed with styled controls and a responsive layout so that the application can be used conveniently by students. :contentReference[oaicite:3]{index=3}

## 7. Frontend Workflow

The frontend follows this workflow:

User Input
↓
Select Learning Task
↓
Submit Request
↓
Send Request to FastAPI
↓
Receive AI Generated Response
↓
Display Result

## 8. Frontend Development Result

The completed frontend provides an interactive interface for accessing the different AI-powered learning features of EduGenie.