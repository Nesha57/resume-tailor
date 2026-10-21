import os
import sys
import json
from typing import List
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

# Pydantic Schemas for Structured Output

class Task(BaseModel):
    task_id: str = Field(description="A unique identifier for the task (e.g., T1, T2).")
    description: str = Field(description="Detailed description of what needs to be done.")
    required_tools: List[str] = Field(description="List of conceptual tools needed (e.g., 'web_search', 'file_reader').")
    risk_assessment: str = Field(description="Potential risks or failure points for this task.")

class Plan(BaseModel):
    goal: str = Field(description="The overall goal being planned for.")
    chronological_tasks: List[Task] = Field(description="An ordered list of tasks to accomplish the goal.")
    success_criteria: str = Field(description="How to determine if the overall goal has been successfully met.")

class AutonomousTaskPlanner:
    def __init__(self):
        self.system_prompt = """
        You are an elite Autonomous Agent Planner.
        Your job is to take a high-level goal from the user and break it down into a highly structured, logical, and chronologically ordered execution plan.
        Think deeply about potential edge cases and necessary tools.
        """

    def generate_plan(self, goal: str) -> dict:
        print(f"🎯 [PLANNING] Analyzing goal: {goal}")
        client = get_client()
        
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Create an execution plan for this goal: {goal}"}
        ]
        
        schema = Plan.model_json_schema()
        
        print("🧠 [THOUGHT] Generating structured plan via Gemini API...")
        response = client.chat.completions.create(
            model=get_model(),
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "agent_plan",
                    "strict": True,
                    "schema": schema
                }
            }
        )
        
        print("📋 [TASK DECOMPOSITION] Plan successfully generated.\n")
        
        content = response.choices[0].message.content
        return json.loads(content)

if __name__ == "__main__":
    print("🤖 [SYSTEM] Starting Exercise 03 Solution")
    
    planner = AutonomousTaskPlanner()
    goal = "Research the latest advancements in quantum computing in 2024 and write a 500-word summary report."
    
    try:
        plan_data = planner.generate_plan(goal)
        
        print("✨ [OUTPUT] Final Execution Plan:\n")
        print(f"**Goal**: {plan_data.get('goal')}")
        print(f"**Success Criteria**: {plan_data.get('success_criteria')}\n")
        
        print("**Tasks**:")
        for task in plan_data.get('chronological_tasks', []):
            print(f"- [{task.get('task_id')}] {task.get('description')}")
            print(f"  Tools: {', '.join(task.get('required_tools', []))}")
            print(f"  Risks: {task.get('risk_assessment')}")
            
    except Exception as e:
        print(f"❌ [ERROR] Failed to generate plan: {e}")
