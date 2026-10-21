import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = None

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ Error: GEMINI_API_KEY not found.")
            sys.exit(1)
        _client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
    return _client

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# TODO: Implement the 5 prompt frameworks using the Role, Objective, Context, Constraints, Format structure.

TECH_RECRUITER_PROMPT = """
TODO: Implement Tech Recruiter Resume Improver
"""

STUDY_PLANNER_PROMPT = """
TODO: Implement Study Planner
"""

TRAVEL_CONCIERGE_PROMPT = """
TODO: Implement Travel Concierge
"""

ENTERPRISE_SUPPORT_PROMPT = """
TODO: Implement Enterprise Support Agent
"""

JUNIOR_CODING_TUTOR_PROMPT = """
TODO: Implement Junior Coding Tutor
"""

def generate_response(system_prompt: str, user_input: str):
    # TODO: Implement chat generation using get_client() and system_prompt
    pass

if __name__ == "__main__":
    print("🤖 [SYSTEM] Starting Exercise 02: Prompt Engineering")
    # TODO: Test one or more of your prompts with a sample user input
