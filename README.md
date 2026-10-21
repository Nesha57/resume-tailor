AI-Powered Resume Tailor

Welcome to the AI Agent Workshop - Day 2! In this hands-on workshop, you'll learn how to build production-ready AI agents using the Google Gemini API.

## Architecture Overview

We use the Google Gemini API (specifically `gemini-2.5-flash`) via the OpenAI Python SDK compatibility mode. This allows us to use standard OpenAI tool calling and structured output formats while leveraging Gemini's speed, context window, and capabilities.

### Key Technologies
- **API Provider:** Google Gemini API
- **Model:** `gemini-2.5-flash`
- **SDK:** `openai` Python SDK (using base_url overrides)
- **Environment:** `python-dotenv` for API key management
- **Data Validation:** `pydantic` for structured output schemas

## Setup & Configuration

1. Get a **FREE** Gemini API Key from Google AI Studio: [https://aistudio.google.com](https://aistudio.google.com)
2. Copy `.env.example` to `.env` and paste your key.
3. Install dependencies from `requirements.txt`.

For detailed step-by-step instructions, see the [RUN_GUIDE.md](./RUN_GUIDE.md).

## Day 2 Schedule (10:00 AM - 4:00 PM)

- **10:00 AM - 10:30 AM**: Setup and Environment Check
- **10:30 AM - 11:30 AM**: First LLM Calls & Structured Output
- **11:30 AM - 12:30 PM**: Tool Calling Essentials
- **12:30 PM - 01:30 PM**: Lunch Break
- **01:30 PM - 02:30 PM**: Memory and Context Management
- **02:30 PM - 03:30 PM**: Multi-Agent Workflows
- **03:30 PM - 04:00 PM**: Review, Testing & Wrap-Up

## Directory Layout

```
.
├── README.md               # This file
├── RUN_GUIDE.md            # Execution and troubleshooting guide
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore rules
├── data/                   # Datasets for exercises
├── day2/                   # Starter code for exercises
├── solutions/              # Completed solutions for exercises
└── tests/                  # Unit tests for the solutions
```

## Security & Environment Rules

1. **NEVER** commit your `.env` file or API keys to version control. The `.gitignore` is pre-configured to ignore `.env` files.
2. The code lazily loads the API client inside functions. This ensures unit tests can import modules without crashing if `GEMINI_API_KEY` is missing in the CI environment.
3. Keep the terminal UI clear and professional. Example logs use planning, execution, and memory banners.
