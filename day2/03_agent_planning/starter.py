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
            print("❌ Error: GEMINI_API_KEY not found.")
            sys.exit(1)
        _client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
    return _client

def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# TODO: Define Pydantic models for Structured Output
# class Task(BaseModel):
#     ...

# class Plan(BaseModel):
#     ...

class AutonomousTaskPlanner:
    def __init__(self):
        # TODO: Initialize planner
        pass

    def generate_plan(self, goal: str):
        print(f"🎯 [PLANNING] Analyzing goal: {goal}")
        # TODO: Construct system prompt for planning
        
        print("🧠 [THOUGHT] Generating structured plan...")
        # TODO: Call Gemini with response_format={"type": "json_schema", ...}
        
        print("📋 [TASK DECOMPOSITION] Plan generated.")
        # TODO: Parse and return the structured plan
        pass

if __name__ == "__main__":
    print("🤖 [SYSTEM] Starting Exercise 03: Autonomous Task Planner")
    
    # TODO: Instantiate planner and generate a plan for a goal
    # planner = AutonomousTaskPlanner()
    # plan = planner.generate_plan("Research the top 3 AI frameworks and write a comparison report.")
    # print(json.dumps(plan, indent=2))
