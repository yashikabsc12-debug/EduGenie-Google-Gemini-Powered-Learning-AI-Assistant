# EduGenie – Quiz Module

## 1. Module Overview

The Quiz module generates multiple-choice questions (MCQs) from a given passage.

## 2. Quiz Generation

EduGenie generates three multiple-choice questions from the given content.

Each question contains four options and a correct answer. :contentReference[oaicite:0]{index=0}

## 3. AI Processing

The Gemini model understands the context and meaning of the given passage and generates relevant questions with plausible options.

## 4. JSON Response

The generated quiz is structured in JSON format for easy integration.

The response is cleaned to remove Markdown code blocks before it is parsed into a Python list. :contentReference[oaicite:1]{index=1}

## 5. Error Handling

If an error occurs during quiz generation or parsing, the module returns an error message for debugging. :contentReference[oaicite:2]{index=2}

## 6. API Endpoint

```text
POST /quiz