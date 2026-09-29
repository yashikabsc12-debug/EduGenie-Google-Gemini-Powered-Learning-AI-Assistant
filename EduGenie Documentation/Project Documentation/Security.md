# EduGenie – Security

## 1. Security Overview

EduGenie follows basic security practices to protect the application's AI service credentials and user-facing system.

## 2. API Key Security

The Gemini API key is stored securely using environment variables.

The API key is not exposed in the frontend code. :contentReference[oaicite:0]{index=0}

## 3. Environment Variables

Sensitive configuration values are stored in the `.env` file instead of being directly written in the application source code.

## 4. GitHub Security

The `.env` file containing the Gemini API key should not be committed or uploaded to the GitHub repository.

## 5. Backend Security

The Gemini API request is handled through the backend.

The frontend does not directly access the Gemini API key.

## 6. Security Result

These practices help prevent accidental exposure of the Gemini API key while developing and sharing the EduGenie project.