# Exercise 07: Autonomous Career Architect Agent

Welcome to Exercise 07! Here, we build our first complete end-to-end agent. It combines planning, file ingestion, Pydantic structured output, and evaluation.

## Objective
Build an Autonomous Career Architect Agent that analyzes a candidate's profile against a target job description and returns a structured gap analysis and preparation plan.

## Concepts Covered
- File ingestion (reading local text files as context)
- System Prompts for persona definition
- Structured Output using Pydantic
- Parsing JSON responses and generating an executive report

## Instructions
1. Open `starter.py` and review the TODOs.
2. Define the `JobAnalysis` Pydantic model exactly as required (match_percentage, strong_matches, missing_skills, interview_questions, preparation_plan, resume_suggestions).
3. Read the contents of `sample_job_description.txt` and `sample_candidate_profile.txt`.
4. Create the system and user messages.
5. Call the Gemini API using OpenAI SDK structured outputs (`response_format` with `json_schema`).
6. Parse and print the executive report.
