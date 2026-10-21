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

def safe_calculator(expression: str) -> str:
    """Safe math evaluator using AST."""
    print(f"🧮 [TOOL EXECUTION] Calculating: {expression}")
    
    # Supported operators
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos
    }

    def eval_node(node):
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.Constant): # for newer Python versions
            return node.value
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return ops[type(node.op)](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return ops[type(node.op)](eval_node(node.operand))
        else:
            raise TypeError(node)
            
    try:
        # We replace % with /100* to handle percentage math roughly if they type '15%'
        expr = expression.replace('%', '/100')
        result = eval_node(ast.parse(expr, mode='eval').body)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

def search_knowledge_base(query: str) -> str:
    """Mock RAG lookup."""
    print(f"🔍 [TOOL EXECUTION] Searching KB for: {query}")
    mock_db = {
        "shipping policy": "Standard shipping takes 3-5 business days. Expedited is 1-2 days.",
        "return policy": "Returns are accepted within 30 days of purchase in original packaging."
    }
    for k, v in mock_db.items():
        if k in query.lower():
            return v
    return "No relevant information found in knowledge base."

def get_user_profile(user_id: str) -> str:
    """Mock DB lookup."""
    print(f"👤 [TOOL EXECUTION] Lookup user: {user_id}")
    users = {
        "U123": {"name": "Alice Smith", "tier": "Premium", "balance": 150.00},
        "U456": {"name": "Bob Jones", "tier": "Standard", "balance": 0.00}
    }
    user = users.get(user_id.upper())
    if user:
        return json.dumps(user)
    return "User not found."


# =====================================================================
# 2. TOOL REGISTRATION
# =====================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "safe_calculator",
            "description": "Evaluates a mathematical expression and returns the result. Use this for all math operations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string", 
                        "description": "Math expression (e.g. '2 + 2', '450 + 300', '15 * 100 / 100')"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": "Searches the internal knowledge base for company policies and general info.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string", 
                        "description": "The search query."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_profile",
            "description": "Retrieves user profile information including name, tier, and balance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string", 
                        "description": "The User ID (e.g., 'U123')."
                    }
                },
                "required": ["user_id"]
            }
        }
    }
]

def execute_tool(name: str, arguments_str: str) -> str:
    """Routes the tool call to the Python function and executes it."""
    try:
        args = json.loads(arguments_str)
        if name == "safe_calculator":
            return safe_calculator(args.get("expression", ""))
        elif name == "search_knowledge_base":
            return search_knowledge_base(args.get("query", ""))
        elif name == "get_user_profile":
            return get_user_profile(args.get("user_id", ""))
        else:
            return f"Unknown tool: {name}"
    except Exception as e:
        return f"Tool execution failed: {str(e)}"


# =====================================================================
# 3. AGENT ENGINE
# =====================================================================

def run_agent(prompt: str, max_iterations: int = 5):
    """Main agent loop that handles tool calls."""
    print(f"\n🚀 [PLANNING] Starting agent task: '{prompt}'")
    
    messages = [{"role": "user", "content": prompt}]
    
    for i in range(max_iterations):
        print(f"\n🔄 [THOUGHT] Agent is thinking... (Iteration {i+1}/{max_iterations})")
        
        response = get_client().chat.completions.create(
            model=get_model(),
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        
        # If there are no tool calls, it means the model has a final answer
        if not message.tool_calls:
            print(f"\n✅ [FINAL ANSWER]\n{message.content}")
            return message.content
            
        # The model requested tool calls
        messages.append(message)
        
        for tool_call in message.tool_calls:
            print(f"🛠️  [TOOL REQUEST] API requested '{tool_call.function.name}' with args: {tool_call.function.arguments}")
            
            # Execute tool locally
            result = execute_tool(tool_call.function.name, tool_call.function.arguments)
            
            print(f"📥 [TOOL RESULT] '{tool_call.function.name}' returned: {result}")
            
            # Append result to messages so the model can see it
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": result
            })
            
    print("\n❌ [ERROR] Max iterations reached without a final answer.")

if __name__ == "__main__":
    prompt = "What is 15% of the total if I have 450 apples and 300 bananas? Also, lookup user ID 'U123' and check the shipping policy."
    run_agent(prompt)
