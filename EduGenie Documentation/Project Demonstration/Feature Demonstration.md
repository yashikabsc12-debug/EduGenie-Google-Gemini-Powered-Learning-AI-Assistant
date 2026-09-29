# EduGenie – Feature Demonstration

## 1. Question and Answer

### Purpose

The Question and Answer feature allows users to ask academic or learning-related questions and receive an AI-generated response.

### Demonstration Steps

1. Open the EduGenie application.
2. Select the QnA option.
3. Enter a question in the input area.
4. Click the Submit button.
5. The question is sent to the FastAPI backend.
6. The backend sends the request to Google Gemini.
7. The generated answer is displayed on the webpage.

### Example Input

What is machine learning?

### Expected Output

The system provides a clear and concise explanation of machine learning.

---

## 2. Topic Explanation

### Purpose

The Explanation feature helps users understand complex topics in a simpler and easier-to-read form.

### Demonstration Steps

1. Open the EduGenie application.
2. Select the Explain option.
3. Enter a topic.
4. Click the Submit button.
5. The request is processed by the backend.
6. The AI generates a simplified explanation.
7. The explanation is displayed to the user.

### Example Input

Explain Artificial Intelligence.

### Expected Output

The system provides a simplified explanation suitable for the selected learning level.

---

## 3. Quiz Generation

### Purpose

The Quiz feature generates multiple-choice questions from a given topic or educational content.

### Demonstration Steps

1. Open the EduGenie application.
2. Select the Quiz option.
3. Enter a topic or educational passage.
4. Select the required learning level.
5. Click the Submit button.
6. The backend sends the request to the AI model.
7. The generated quiz is displayed on the webpage.

### Example Input

Python programming basics.

### Expected Output

The system generates multiple-choice questions with answer options for self-assessment.

---

## 4. Text Summarization

### Purpose

The Summarization feature converts lengthy educational content into a concise summary.

### Demonstration Steps

1. Open the EduGenie application.
2. Select the Summary option.
3. Enter or paste a paragraph.
4. Click the Submit button.
5. The content is sent to the backend.
6. Google Gemini processes the content.
7. A concise summary is displayed.

### Example Input

A long paragraph about Artificial Intelligence or Machine Learning.

### Expected Output

The system provides a shorter version containing the important information.

---

## 5. Personalized Learning Path

### Purpose

The Learning Path feature provides structured learning recommendations based on the user's topic, level, and learning goal.

### Demonstration Steps

1. Open the EduGenie application.
2. Select the Recommend Path option.
3. Enter the topic to learn.
4. Select the learning level.
5. Enter the learning goal if required.
6. Click the Submit button.
7. The request is processed by the AI model.
8. A structured learning path is displayed.

### Example Input

Topic: Data Science

Level: Beginner

Goal: Learn Data Science from basics.

### Expected Output

The system provides a structured learning sequence from basic concepts towards advanced concepts along with learning guidance.

---

## 6. Backend API Demonstration

EduGenie provides separate REST API endpoints for its major functionalities.

The main endpoints are:

- POST /qa
- POST /explain
- POST /quiz
- POST /summarize
- POST /learn/recommendations

These endpoints connect the web interface with the backend processing and AI functionality.

## 7. Frontend Demonstration

The EduGenie frontend provides:

- Task selection
- User input area
- Learning level selection
- Submit button
- Result display area

The frontend sends requests to the FastAPI backend and displays the generated response to the user.

## 8. Overall Demonstration Flow

User selects a feature
↓
User enters learning content
↓
User submits the request
↓
Frontend sends request to FastAPI
↓
FastAPI processes the request
↓
Google Gemini generates the response
↓
Response is returned to frontend
↓
Result is displayed to the user