# Exercise 01: Gemini Client & API Handler (First LLM Call)

## Overview
Welcome to your first step in building AI agents! In this exercise, you'll establish the foundation for all future work by setting up a robust, production-ready client to interact with the Gemini API.

We will use the **OpenAI Python SDK** in compatibility mode, pointing it to the Gemini API endpoint. This provides a standard interface that is widely used across the industry.

## Architecture & Setup
We use the OpenAI SDK compatibility layer to connect to the Gemini API.

**Base URL**: `https://generativelanguage.googleapis.com/v1beta/openai/`
**API Key Env Var**: `GEMINI_API_KEY`
**Default Model**: `gemini-2.5-flash`

## Steps
1. Create a `.env` file in the root of your project.
2. Add your API key: `GEMINI_API_KEY=your_key_here`. Get a key from [Google AI Studio](https://aistudio.google.com).
3. Review `starter.py` and implement the `TODO` sections.
4. Run your script to ensure you can communicate with the Gemini API.

## Checkpoint Questions
- Why do we use the OpenAI SDK to call Gemini? (Hint: standard interface, ecosystem compatibility).
- What happens if the API key is missing? How does your code handle it gracefully?

## Stretch Goals
- Implement a simple interactive loop (CLI chatbot).
- Add robust error handling (retries, rate limit awareness).
- Track and print token usage and timing for each call.
