import os
import sys
import json
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import OpenAI

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

# TODO: Define your Pydantic model here. 
# It should have fields for: title, executive_summary, target_audience, 
# section_breakdown (list of strings), quality_checks (list of strings), 
# seo_keywords (list of strings), call_to_action, and read_time (int).
class ContentPlan(BaseModel):
    pass

def generate_content_plan(topic: str):
    print(f"\n📝 Generating Content Plan for: '{topic}'...\n")
    
    # TODO: Get the JSON schema from the Pydantic model
    # schema = ContentPlan.model_json_schema()
    
    messages = [
        {"role": "system", "content": "You are an expert Content Architect. Create comprehensive content plans."},
        {"role": "user", "content": f"Create a detailed content plan for a blog post about: {topic}"}
    ]
    
    # TODO: Call the API with the response_format parameter set to JSON schema mode
    
    # TODO: Parse the returned JSON string back into the ContentPlan Pydantic model
    
    # TODO: Print a nicely formatted report of the content plan
    
    print("Not implemented yet.")


if __name__ == "__main__":
    generate_content_plan("How AI Agents Will Transform Software Engineering in 2026")
