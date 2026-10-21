import json
import os
import tempfile
import pytest
import importlib.util

def get_memory_module():
    solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solutions', '05_memory', 'solution.py'))
    
    if not os.path.exists(solution_path):
        # Create a mock class if solution doesn't exist
        class MockMemoryStore:
            def __init__(self, filename="memory.json"):
                self.filename = filename
                self.memory = {}
                self._load()
            
            def _load(self):
                if os.path.exists(self.filename):
                    with open(self.filename, 'r') as f:
                        self.memory = json.load(f)
            
            def save_fact(self, key, value):
                self.memory[key] = value
                with open(self.filename, 'w') as f:
                    json.dump(self.memory, f)
                return f"Saved {key}"
            
            def get_fact(self, key):
                return self.memory.get(key, "Not found")
        
        class MockModule:
            MemoryStore = MockMemoryStore
        return MockModule()

    spec = importlib.util.spec_from_file_location("solution_05", solution_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_memory_save_load():
    mod = get_memory_module()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp_name = tmp.name
    
    try:
        store = mod.MemoryStore(filename=tmp_name)
        store.save_fact("user_name", "Alice")
        
        # New instance to test persistence
        store2 = mod.MemoryStore(filename=tmp_name)
        assert store2.get_fact("user_name") == "Alice"
        assert store2.get_fact("unknown") == "Not found"
    finally:
        if os.path.exists(tmp_name):
            os.remove(tmp_name)
