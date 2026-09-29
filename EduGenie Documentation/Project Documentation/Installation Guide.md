# EduGenie – Installation Guide

## 1. Prerequisites

- Python 3.10 or above
- Visual Studio Code
- Google Gemini API Key
- Internet connection

## 2. Project Setup

Open the EduGenie project folder in Visual Studio Code.

## 3. Create Virtual Environment

```text
python -m venv .venv

4. Activate Virtual Environment

For Windows:

.venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Configure Gemini API Key

Create a .env file in the project root folder.

Add the Gemini API key:

GEMINI_API_KEY=your_api_key_here

The API key should be kept private and should not be committed to GitHub.

7. Run the Application
uvicorn main:app --reload
8. Open the Application

Open the local application in a web browser:

http://127.0.0.1:8001
9. Test the Application

Select a learning feature, enter the required input, and submit the request.

Verify that the generated response is displayed correctly.