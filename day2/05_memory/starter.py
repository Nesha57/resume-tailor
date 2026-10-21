import os
import sys
import json
from datetime import datetime
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

class AgentMemoryStore:
    def __init__(self, filepath: str = "memory.json"):
        self.filepath = filepath
        self.data = {}
        # TODO: Load data from file if it exists

    def _load(self):
        # TODO: Implement loading logic
        pass

    def _save(self):
        # TODO: Implement saving logic
        pass

    def remember(self, key: str, value: str):
        # TODO: Store value with a timestamp and save
        pass

    def recall(self, key: str):
        # TODO: Return value if key exists
        return None

    def get_all(self):
        # TODO: Return all memories
        return {}

    def format_for_prompt(self) -> str:
        # TODO: Format memories into a string to inject into the system prompt
        return ""

def chat_loop():
    print("🧠 Memory Agent Started (type 'exit' to quit)")
    print("Commands: /remember <key> <value> | /show | <chat message>")
    
    # TODO: Initialize memory store and history
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input or user_input.lower() == 'exit':
                break
                
            # TODO: Handle commands and chat logic
                
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    chat_loop()
