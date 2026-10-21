# Troubleshooting Guide

## 1. API Key Not Found
**Symptom:** `openai.AuthenticationError` or script exits saying key is missing.
**Fix:** Ensure `.env` is in the same directory as the script being run, or export it in the terminal:
`export GEMINI_API_KEY="AIza..."` (Linux/Mac)
`set GEMINI_API_KEY="AIza..."` (Windows)

## 2. Pydantic Schema Errors
**Symptom:** Validation errors when parsing JSON.
**Fix:** Ensure `strict: True` in `response_format` and check that the LLM didn't wrap the JSON in Markdown backticks.

## 3. Tool Calling Infinite Loops
**Symptom:** Agent keeps calling the same tool over and over.
**Fix:** Ensure the tool result is correctly appended to the `messages` array with `role="tool"` and the correct `tool_call_id`.

## 4. Rate Limits (429 Errors)
**Symptom:** API returns 429 Too Many Requests.
**Fix:** Tell students to wait 60 seconds. Free tier Gemini API has RPM limits.
