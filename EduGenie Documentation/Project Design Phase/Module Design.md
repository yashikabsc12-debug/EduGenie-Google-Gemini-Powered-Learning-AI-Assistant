# EduGenie – Module Design

## 1. Overview

EduGenie is divided into functional modules. Each module performs a specific learning-related task.

## 2. Question and Answer Module

### Purpose

To provide answers to academic and learning-related questions.

### Input

A question provided by the user.

### Processing

The question is sent to the backend and processed using Google Gemini.

### Output

An AI-generated answer is returned to the user.

---

## 3. Explanation Module

### Purpose

To explain complex topics in a simple and understandable manner.

### Input

A topic provided by the user.

### Processing

The topic and learner level are processed by the AI service.

### Output

A simplified explanation is returned.

---

## 4. Quiz Module

### Purpose

To generate multiple-choice questions for self-assessment.

### Input

A topic or educational content.

### Processing

The AI model generates questions and answer options based on the provided content.

### Output

A structured quiz containing questions and options.

---

## 5. Summary Module

### Purpose

To convert lengthy educational content into a concise summary.

### Input

A paragraph or educational passage.

### Processing

The content is processed by the AI service to identify and retain important information.

### Output

A concise summary is returned.

---

## 6. Learning Path Module

### Purpose

To provide structured learning recommendations.

### Input

- Topic
- Learning level
- Learning goal

### Processing

The AI generates a structured sequence of concepts based on the user's requirements.

### Output

A personalized learning path is returned.

---

## 7. Frontend Module

### Purpose

To provide the user interface for interacting with EduGenie.

### Main Components

- Task selection
- Text input
- Learning level selection
- Submit button
- Result display

---

## 8. Backend Module

### Purpose

To receive requests from the frontend, process them, communicate with the AI service, and return responses.

### Framework

FastAPI

---

## 9. AI Integration Module

### Purpose

To connect the EduGenie backend with Google Gemini.

### Responsibility

- Send prompts to the AI model.
- Receive generated responses.
- Process the generated output.
- Return the result to the appropriate API endpoint.