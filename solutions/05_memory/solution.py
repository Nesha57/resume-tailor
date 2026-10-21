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
    """A production-ready memory store that saves key-value facts to a JSON file."""
    
    def __init__(self, filepath: str = "memory.json", filename: str = None):
        self.filepath = filename if filename is not None else filepath
        self.data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.data = json.load(f)
                print(f"📁 [MEMORY STORE] Loaded {len(self.data)} memories from {self.filepath}")
            except Exception as e:
                print(f"⚠️ [MEMORY STORE] Error loading memory: {e}")
                self.data = {}
        else:
            print("📁 [MEMORY STORE] Initialized new empty memory store.")

    def _save(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"⚠️ [MEMORY STORE] Error saving memory: {e}")

    def remember(self, key: str, value: str):
        """Stores a memory with a timestamp."""
        self.data[key] = {
            "value": value,
            "updated_at": datetime.now().isoformat()
        }
        self._save()
        print(f"💾 [MEMORY STORE] Remembered: {key} -> {value}")

    def recall(self, key: str):
        """Recalls a specific memory."""
        entry = self.data.get(key)
        if isinstance(entry, dict) and "value" in entry:
            return entry["value"]
        return entry

    def save_fact(self, key: str, value: str):
        self.remember(key, value)

    def get_fact(self, key: str):
        res = self.recall(key)
        return res if res is not None else "Not found"

    def get_all(self):
        return self.data

    def format_for_prompt(self) -> str:
        """Formats the persistent memory for injection into the system prompt."""
        if not self.data:
            return "No prior memories recorded."
            
        lines = []
        for key, entry in self.data.items():
            lines.append(f"- {key}: {entry['value']} (Updated: {entry['updated_at'][:10]})")
        return "\n".join(lines)


# Alias for compatibility with tests
MemoryStore = AgentMemoryStore


def chat_loop():
    print("🧠 Memory Agent Started (type 'exit' to quit)")
    print("Commands: /remember <key> <value> | /show | <chat message>")
    
    memory = AgentMemoryStore()
    
    # We maintain a sliding window of conversation history (short-term memory)
    # in addition to our persistent long-term memory store.
    history = []
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            if not user_input or user_input.lower() in ['exit', 'quit']:
                break
                
            # --- CLI Command Handling ---
            if user_input.startswith("/remember "):
                parts = user_input[10:].split(" ", 1)
                if len(parts) == 2:
                    memory.remember(parts[0], parts[1])
                else:
                    print("Usage: /remember <key> <value>")
                continue
                
            elif user_input == "/show":
                print("\n📚 Current Memories:")
                for k, v in memory.get_all().items():
                    print(f"  - {k}: {v['value']}")
                continue
                
            # --- Normal Chat Flow ---
            
            # Inject persistent memory into the system prompt dynamically on every turn
            system_prompt = f"""You are a helpful AI assistant with access to long-term memory.
Use the following facts about the user/domain if they are relevant to the conversation.

<long_term_memory>
{memory.format_for_prompt()}
</long_term_memory>"""

            messages = [{"role": "system", "content": system_prompt}]
            
            # Add short-term conversational history
            messages.extend(history[-10:]) # Keep last 10 messages
            
            # Add current user message
            messages.append({"role": "user", "content": user_input})
            history.append({"role": "user", "content": user_input})
            
            print("🤖 Agent is thinking...")
            response = get_client().chat.completions.create(
                model=get_model(),
                messages=messages
            )
            
            reply = response.choices[0].message.content
            print(f"\n✨ Agent: {reply}")
            
            history.append({"role": "assistant", "content": reply})
                
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    chat_loop()
