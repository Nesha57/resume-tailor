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
            print("Please create a .env file based on .env.example and set your API key.")
            print("Get a free key from Google AI Studio: https://aistudio.google.com")
            sys.exit(1)
        _client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
    return _client

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

class JobAnalysis(BaseModel):
    match_percentage: int = Field(description="Estimated match percentage (0-100)")
    strong_matches: list[str] = Field(description="List of skills/experience that match well")
    missing_skills: list[str] = Field(description="List of required skills the candidate is missing")
    interview_questions: list[str] = Field(description="Suggested interview questions to assess the candidate")
    preparation_plan: list[str] = Field(description="Actionable steps for the candidate to prepare for this role")
    resume_suggestions: list[str] = Field(description="Suggestions to improve the candidate's resume for this role")

def load_file(filename: str) -> str:
    """Helper to load a text file."""
    # Look for the file in the current directory or the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Adjust path if we're running from solutions/
    if 'solutions' in script_dir:
        target_path = os.path.join(script_dir, '..', '..', 'day2', '07_first_agent', filename)
    else:
        target_path = os.path.join(script_dir, filename)
        
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ Warning: Could not find {filename} at {target_path}")
        return ""

def analyze_candidate(job_desc: str, candidate_profile: str) -> JobAnalysis:
    """Analyze the candidate against the job description using Gemini."""
    client = get_client()
    
    messages = [
        {"role": "system", "content": "You are an expert technical recruiter and career coach. Your job is to analyze a candidate's profile against a specific job description. Provide an honest, highly constructive analysis."},
        {"role": "user", "content": f"Please perform a gap analysis.\n\nJOB DESCRIPTION:\n{job_desc}\n\nCANDIDATE PROFILE:\n{candidate_profile}"}
    ]
    
    print("🤖 [THOUGHT] Analyzing candidate profile against job description...")
    
    schema = JobAnalysis.model_json_schema()
    
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "job_analysis_schema",
                "strict": True,
                "schema": schema
            }
        },
        temperature=0.2
    )
    
    # Parse the structured JSON response
    result_json = response.choices[0].message.content
    analysis_dict = json.loads(result_json)
    return JobAnalysis(**analysis_dict)

def run():
    print("🚀 [PLANNING] Starting Autonomous Career Architect Agent...")
    
    print("📄 [MEMORY STORE] Loading job description and candidate profile...")
    job_desc = load_file("sample_job_description.txt")
    candidate_profile = load_file("sample_candidate_profile.txt")
    
    if not job_desc or not candidate_profile:
        print("❌ Error: Sample files not found. Make sure sample_job_description.txt and sample_candidate_profile.txt exist.")
        return

    analysis = analyze_candidate(job_desc, candidate_profile)
    
    print("\n✅ [OUTPUT] Executive Report Generated:")
    print("=" * 50)
    print(f"⭐ Match Percentage: {analysis.match_percentage}%")
    print("\n✅ Strong Matches:")
    for match in analysis.strong_matches:
        print(f"  - {match}")
    
    print("\n⚠️ Missing Skills/Gaps:")
    for gap in analysis.missing_skills:
        print(f"  - {gap}")
        
    print("\n📝 Resume Improvement Suggestions:")
    for suggestion in analysis.resume_suggestions:
        print(f"  - {suggestion}")
        
    print("\n🏋️ Preparation Plan (Next 30 Days):")
    for step in analysis.preparation_plan:
        print(f"  - {step}")
        
    print("\n❓ Anticipated Interview Questions:")
    for q in analysis.interview_questions:
        print(f"  - {q}")
    print("=" * 50)

if __name__ == "__main__":
    run()
