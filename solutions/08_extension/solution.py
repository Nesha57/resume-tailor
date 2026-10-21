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

# ==========================================
# OPTION E: Confidence & Self-Evaluation Scoring
# ==========================================
class EnhancedJobAnalysis(BaseModel):
    match_percentage: int = Field(description="Estimated match percentage (0-100)")
    strong_matches: list[str] = Field(description="List of skills/experience that match well")
    missing_skills: list[str] = Field(description="List of required skills the candidate is missing")
    preparation_plan: list[str] = Field(description="Actionable steps for the candidate to prepare for this role")
    confidence_score: int = Field(description="Agent's confidence in this assessment (0-100)")
    reasoning: str = Field(description="Explanation of the confidence score and overall assessment")

# ==========================================
# OPTION A: Salary Calculator Tool
# ==========================================
def calculate_estimated_salary(role: str, experience_years: float, location: str) -> str:
    """Tool function to estimate salary."""
    print(f"🛠️ [TOOL EXECUTION] Calculating salary for {role} ({experience_years} yrs) in {location}...")
    base = 100000
    if "senior" in role.lower():
        base += 40000
    base += experience_years * 5000
    if location.lower() in ["sf", "ny", "seattle"]:
        base *= 1.2
    
    return f"${int(base):,} - ${int(base * 1.1):,}"

salary_tool = {
    "type": "function",
    "function": {
        "name": "calculate_estimated_salary",
        "description": "Calculate estimated salary for a given role, experience level, and location.",
        "parameters": {
            "type": "object",
            "properties": {
                "role": {"type": "string"},
                "experience_years": {"type": "number"},
                "location": {"type": "string"}
            },
            "required": ["role", "experience_years", "location"]
        }
    }
}

# ==========================================
# OPTION D: HR Policy RAG Engine
# ==========================================
def retrieve_hr_policies(query: str) -> str:
    print(f"📚 [MEMORY STORE] Retrieving HR policies for: {query}")
    policies = {
        "remote": "Remote work is allowed up to 3 days a week.",
        "relocation": "Relocation assistance up to $5,000 is provided for senior roles.",
        "learning": "Annual learning stipend of $1,000 available for continuous education."
    }
    
    relevant = []
    for k, v in policies.items():
        if k in query.lower():
            relevant.append(v)
            
    if not relevant:
        return "Standard company policies apply."
    return " ".join(relevant)

rag_tool = {
    "type": "function",
    "function": {
        "name": "retrieve_hr_policies",
        "description": "Retrieve HR policies based on a keyword query like 'remote', 'relocation', or 'learning'.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    }
}

# ==========================================
# OPTION C: Multi-Stage Critic Loop
# ==========================================
def critique_analysis(draft_analysis_json: str) -> EnhancedJobAnalysis:
    """Have the model act as a senior HR director critiquing and refining the output."""
    client = get_client()
    print("🤖 [THOUGHT] Running critique loop on draft analysis...")
    
    schema = EnhancedJobAnalysis.model_json_schema()
    
    messages = [
        {"role": "system", "content": "You are a Senior HR Director. Review the following draft candidate assessment. Refine it to be more precise, objective, and actionable. Output the final refined JSON."},
        {"role": "user", "content": f"DRAFT ANALYSIS:\n{draft_analysis_json}"}
    ]
    
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "enhanced_job_analysis_schema",
                "strict": True,
                "schema": schema
            }
        },
        temperature=0.2
    )
    
    result_json = response.choices[0].message.content
    analysis_dict = json.loads(result_json)
    return EnhancedJobAnalysis(**analysis_dict)

# ==========================================
# OPTION B: Persistent Candidate Memory (Main Loop)
# ==========================================
def generate_initial_draft(job_desc: str, candidate_profile: str) -> str:
    """Generate the initial draft using the standard schema."""
    client = get_client()
    messages = [
        {"role": "system", "content": "You are a technical recruiter. Provide a comprehensive gap analysis."},
        {"role": "user", "content": f"JOB DESCRIPTION:\n{job_desc}\n\nCANDIDATE PROFILE:\n{candidate_profile}"}
    ]
    
    schema = EnhancedJobAnalysis.model_json_schema()
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "enhanced_job_analysis_schema",
                "strict": True,
                "schema": schema
            }
        },
        temperature=0.2
    )
    return response.choices[0].message.content

def interactive_chat(initial_context: str):
    """CLI loop for chatting with the agent after the report is generated."""
    client = get_client()
    print("\n💬 [INTERACTIVE] The HR Assistant is ready for questions (type 'exit' to quit).")
    
    messages = [
        {"role": "system", "content": "You are an HR Assistant with access to candidate context, salary data, and HR policies. Use tools to answer questions."},
        {"role": "user", "content": f"Here is the context of the candidate we just reviewed:\n{initial_context}"},
        {"role": "assistant", "content": "I understand the context. How can I help you with this candidate?"}
    ]
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            messages.append({"role": "user", "content": user_input})
            
            response = client.chat.completions.create(
                model=get_model(),
                messages=messages,
                tools=[salary_tool, rag_tool],
                tool_choice="auto"
            )
            
            msg = response.choices[0].message
            
            if msg.tool_calls:
                messages.append(msg)
                for tool_call in msg.tool_calls:
                    func_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    
                    if func_name == "calculate_estimated_salary":
                        result = calculate_estimated_salary(**args)
                    elif func_name == "retrieve_hr_policies":
                        result = retrieve_hr_policies(**args)
                    else:
                        result = "Unknown tool."
                        
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": func_name,
                        "content": result
                    })
                    
                # Second turn
                response = client.chat.completions.create(
                    model=get_model(),
                    messages=messages
                )
                final_reply = response.choices[0].message.content
                print(f"🤖 HR Assistant: {final_reply}")
                messages.append({"role": "assistant", "content": final_reply})
                
            else:
                reply = msg.content
                print(f"🤖 HR Assistant: {reply}")
                messages.append({"role": "assistant", "content": reply})
                
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


def run():
    print("🚀 [PLANNING] Starting Extended Enterprise Agent...")
    
    # Mock data for demonstration
    job_desc = "Senior Backend Engineer. 5+ years Python, distributed systems. Location: Seattle."
    candidate_profile = "Alex Chen. 3.5 years Python. Wants to relocate to Seattle."
    
    print("🤖 [THOUGHT] Generating initial draft analysis...")
    draft = generate_initial_draft(job_desc, candidate_profile)
    
    print("🤖 [THOUGHT] Critic loop processing...")
    final_report = critique_analysis(draft)
    
    print("\n✅ [OUTPUT] Final Executive Report (After Critique):")
    print("=" * 50)
    print(f"⭐ Match Percentage: {final_report.match_percentage}%")
    print(f"🧠 Confidence Score: {final_report.confidence_score}%")
    print(f"📝 Reasoning: {final_report.reasoning}")
    print("=" * 50)
    
    # Pass context into the interactive chat
    context = final_report.model_dump_json(indent=2)
    interactive_chat(context)

if __name__ == "__main__":
    run()
