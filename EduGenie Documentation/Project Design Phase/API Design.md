# EduGenie – API Design

## 1. Overview

EduGenie uses FastAPI to provide REST API endpoints for communication between the frontend and backend.

## 2. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /qa | Question and Answer |
| POST | /explain | Topic Explanation |
| POST | /quiz | Quiz Generation |
| POST | /summarize | Text Summarization |
| POST | /learn/recommendations | Learning Recommendations |

## 3. Question and Answer API

### Endpoint

POST /qa

### Purpose

Accepts a learning question and returns an AI-generated answer.

### Input

- Question
- Learning level

### Output

AI-generated answer.

---

## 4. Explanation API

### Endpoint

POST /explain

### Purpose

Provides a simplified explanation of a given topic.

### Input

- Topic
- Learning level

### Output

AI-generated explanation.

---

## 5. Quiz API

### Endpoint

POST /quiz

### Purpose

Generates a quiz from the provided topic or content.

### Input

- Topic or content
- Learning level
- Number of questions

### Output

Generated quiz questions and answer options.

---

## 6. Summary API

### Endpoint

POST /summarize

### Purpose

Summarizes the provided educational content.

### Input

- Text

### Output

Concise summary.

---

## 7. Learning Recommendations API

### Endpoint

POST /learn/recommendations

### Purpose

Generates a structured learning path.

### Input

- Topic
- Learning level
- Learning goal

### Output

AI-generated learning recommendations.

## 8. API Documentation

FastAPI automatically provides interactive API documentation.

The documentation can be accessed through:

/docs

## 9. Backend Communication

The frontend sends HTTP POST requests to the appropriate endpoint. The FastAPI backend processes the request and returns the generated result to the frontend.