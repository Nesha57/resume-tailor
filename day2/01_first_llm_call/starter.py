import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

# TODO: Load environment variables from .env file

_client = None

def get_client():
    """
    Initialize and return the OpenAI client configured for Gemini.
    """
    global _client
    if _client is None:
        # TODO: Get GEMINI_API_KEY from environment
        
        # TODO: Handle missing API key gracefully
        
        # TODO: Initialize OpenAI client with Gemini base_url and api_key
        pass
    return _client

def get_model():
    # TODO: Return model from environment GEMINI_MODEL, default to 'gemini-2.5-flash'
    pass

def send_chat_message(prompt: str):
    """
    Send a chat message to Gemini and return the response.
    """
    # TODO: Get client and model
    
    # TODO: Record start time
    
    # TODO: Create chat completion request with system prompt and user prompt
    
    # TODO: Record end time and calculate duration
    
    # TODO: Extract and print token usage and timing
    
    # TODO: Return the content of the response
    pass

if __name__ == "__main__":
    print("🤖 [SYSTEM] Starting Exercise 01: First LLM Call")
    # TODO: Implement a simple test call
    # response = send_chat_message("Hello, Gemini! Are you ready for Day 2?")
    # print(f"\n[OUTPUT]: {response}")
