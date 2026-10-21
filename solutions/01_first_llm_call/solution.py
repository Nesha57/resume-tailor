import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError

load_dotenv()

_client = None

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ [ERROR] GEMINI_API_KEY not found in environment variables.")
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

def send_chat_message(prompt: str, max_retries: int = 3):
    client = get_client()
    model = get_model()
    
    messages = [
        {"role": "system", "content": "You are a helpful, expert AI assistant."},
        {"role": "user", "content": prompt}
    ]
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 [THOUGHT] Sending prompt to {model}...")
            start_time = time.time()
            
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
            
            duration = time.time() - start_time
            usage = response.usage
            
            print(f"⏱️ [METRICS] Request took {duration:.2f}s")
            if usage:
                print(f"📊 [METRICS] Tokens - Prompt: {usage.prompt_tokens}, Completion: {usage.completion_tokens}, Total: {usage.total_tokens}")
                
            return response.choices[0].message.content
            
        except RateLimitError:
            wait_time = 2 ** attempt
            print(f"⚠️ [WARNING] Rate limit hit. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except APIConnectionError as e:
            print(f"❌ [ERROR] Connection error: {e}")
            break
        except Exception as e:
            print(f"❌ [ERROR] Unexpected error: {e}")
            break
            
    return None

if __name__ == "__main__":
    print("🤖 [SYSTEM] Starting Exercise 01 Solution")
    print("Type 'exit' or 'quit' to end the interactive loop.\n")
    
    while True:
        try:
            user_input = input("\n👤 You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("👋 Goodbye!")
                break
                
            if not user_input.strip():
                continue
                
            response = send_chat_message(user_input)
            if response:
                print(f"\n✨ [OUTPUT]\n{response}")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break