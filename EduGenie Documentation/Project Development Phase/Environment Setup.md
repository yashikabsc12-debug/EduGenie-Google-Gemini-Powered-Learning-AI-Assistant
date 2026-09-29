# EduGenie – Environment Setup

## 1. Development Environment

EduGenie was developed using Python and FastAPI for the backend and HTML, CSS, and JavaScript for the frontend.

## 2. Prerequisites

The following software and tools are required:

- Python 3.10+
- FastAPI
- Uvicorn
- Jinja2
- Google Gemini API
- HTML
- CSS
- JavaScript

## 3. Backend Setup

A Python virtual environment was created to manage the project dependencies.

The required Python packages were installed using the project's requirements file.

## 4. Gemini API Setup

A Google Gemini API key was required for connecting EduGenie with the Gemini AI service.

The API key was stored securely using environment variables instead of exposing it in the frontend code.

## 5. Project Structure

The project contains separate components for:

- FastAPI backend
- AI service integration
- Request and response models
- HTML templates
- CSS styling
- JavaScript functionality
- Testing

## 6. Running the Application

The EduGenie application can be started using Uvicorn.

```text
uvicorn main:app --reload