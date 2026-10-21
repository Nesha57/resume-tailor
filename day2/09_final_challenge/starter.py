import os
import sys
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()

_client = None

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ Error: GEMINI_API_KEY not found in environment variables.")
            sys.exit(1)
        _client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
    return _client

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# ==========================================
# 1. Pydantic Schema for Structured Output
# ==========================================
# TODO: Define StudyPlan schema (weekly_schedule, recommended_resources, diagnostic_quiz)

# ==========================================
# 2. Tool Definition
# ==========================================
def calculate_study_hours(days_until_exam: int, current_knowledge_level: str) -> int:
    """Tool to calculate total recommended study hours."""
    # TODO: implement simple logic
    return 10

# TODO: define OpenAI tool schema for calculate_study_hours

# ==========================================
# 3. Agent Logic
# ==========================================
def generate_study_plan(subject: str, days_until_exam: int, level: str):
    """Generate the study plan and quiz using tools and structured output."""
    client = get_client()
    # TODO: Build messages, call tools, get structured output
    pass

# ==========================================
# 4. Interactive CLI Loop
# ==========================================
def interactive_quiz_loop(plan):
    """Administer the quiz and grade it."""
    # TODO: Loop through quiz questions, get user input, send to LLM for grading
    pass

def run():
    print("🚀 Starting Study Planner Agent...")
    # TODO: gather user input, generate plan, run quiz loop
    
if __name__ == "__main__":
    run()
