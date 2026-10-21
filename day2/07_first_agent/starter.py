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

# TODO: Define the JobAnalysis Pydantic model.
# Requirements:
# - match_percentage: int (0-100)
# - strong_matches: list[str]
# - missing_skills: list[str]
# - interview_questions: list[str]
# - preparation_plan: list[str]
# - resume_suggestions: list[str]
class JobAnalysis(BaseModel):
    pass

def load_file(filename: str) -> str:
    """Helper to load a text file."""
    # TODO: read the file contents
    return ""

def analyze_candidate(job_desc: str, candidate_profile: str) -> JobAnalysis:
    """Analyze the candidate against the job description using Gemini."""
    client = get_client()
    
    # TODO: Construct the messages (system prompt + user prompt with file contents)
    messages = []
    
    print("🤖 [THOUGHT] Analyzing candidate profile against job description...")
    
    # TODO: Call Gemini API using response_format for Structured Output (JobAnalysis schema)
    # response = ...
    
    # TODO: Parse the JSON response into the Pydantic model
    # return parsed_model
    pass

def run():
    print("🚀 [PLANNING] Starting Autonomous Career Architect Agent...")
    
    # TODO: load sample_job_description.txt and sample_candidate_profile.txt
    
    # analysis = analyze_candidate(job_desc, candidate_profile)
    
    print("\n✅ [OUTPUT] Executive Report Generated:")
    # TODO: Print a formatted report based on the analysis
    
if __name__ == "__main__":
    run()
