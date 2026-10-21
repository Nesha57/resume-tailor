import os
import sys
import json
import ast
import operator
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


# =====================================================================
# 1. TOOL IMPLEMENTATIONS
# =====================================================================

def calculator(expression: str) -> str:
    """Safe math evaluator using AST."""
    # TODO: Implement a safe math evaluator that takes a string like '2 + 2' and returns '4'.
    return "Not implemented"

def search_knowledge_base(query: str) -> str:
    """Mock RAG lookup."""
    # TODO: Implement a mock search function that returns results based on the query.
    return "Not implemented"

def get_user_profile(user_id: str) -> str:
    """Mock DB lookup."""
    # TODO: Implement a mock database lookup for a user ID.
    return "Not implemented"


# =====================================================================
# 2. TOOL REGISTRATION
# =====================================================================

# TODO: Define the tools list for the OpenAI compatible API.
tools = [
    # Add function definitions here
]


def execute_tool(name: str, arguments_str: str) -> str:
    """Routes the tool call to the Python function and executes it."""
    # TODO: Parse the arguments_str as JSON, route to the correct function, 
    # execute it, and return the result as a string.
    return "Not implemented"


# =====================================================================
# 3. AGENT ENGINE
# =====================================================================

def run_agent(prompt: str, max_iterations: int = 5):
    """Main agent loop that handles tool calls."""
    print(f"\n🚀 [PLANNING] Starting agent task: '{prompt}'")
    
    messages = [{"role": "user", "content": prompt}]
    
    for i in range(max_iterations):
        # TODO: Call the API with messages and tools
        # TODO: Handle the response. If it's a tool call, execute it and append the result.
        # TODO: If it's a final answer, print and return it.
        pass
        
    print("❌ [ERROR] Max iterations reached without a final answer.")

if __name__ == "__main__":
    prompt = "What is 15% of the total if I have 450 apples and 300 bananas? Also, lookup user ID 'U123'."
    run_agent(prompt)
