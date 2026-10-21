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
# 1. Pydantic Schema for Structured Output
# ==========================================
class QuizQuestion(BaseModel):
    question: str = Field(description="The question text")
    options: list[str] = Field(description="List of multiple choice options (A, B, C, D)")
    correct_answer: str = Field(description="The correct option (A, B, C, or D)")

class StudyPlan(BaseModel):
    total_hours_recommended: int = Field(description="Total study hours recommended by the calculator tool")
    weekly_schedule: list[str] = Field(description="Breakdown of what to study each week")
    recommended_resources: list[str] = Field(description="List of books, websites, or courses")
    diagnostic_quiz: list[QuizQuestion] = Field(description="A 3-question diagnostic quiz")

# ==========================================
# 2. Tool Definition
# ==========================================
def calculate_study_hours(days_until_exam: int, current_knowledge_level: str) -> int:
    """Tool to calculate total recommended study hours."""
    print(f"🛠️ [TOOL EXECUTION] Calculating hours for {days_until_exam} days, level: {current_knowledge_level}...")
    base_hours = 100
    if current_knowledge_level.lower() == "beginner":
        base_hours = 150
    elif current_knowledge_level.lower() == "advanced":
        base_hours = 50
        
    # Scale based on time constraint (cramming requires denser hours)
    weeks = max(1, days_until_exam / 7)
    hours_per_week = base_hours / weeks
    
    # Cap at realistic max (40 hours a week)
    if hours_per_week > 40:
        return 40 * int(weeks)
    return int(base_hours)

study_tool = {
    "type": "function",
    "function": {
        "name": "calculate_study_hours",
        "description": "Calculate total required study hours based on time until exam and current knowledge level.",
        "parameters": {
            "type": "object",
            "properties": {
                "days_until_exam": {"type": "integer"},
                "current_knowledge_level": {"type": "string"}
            },
            "required": ["days_until_exam", "current_knowledge_level"]
        }
    }
}

# ==========================================
# 3. Agent Logic
# ==========================================
def generate_study_plan(subject: str, days_until_exam: int, level: str) -> StudyPlan:
    """Generate the study plan and quiz using tools and structured output."""
    client = get_client()
    print(f"🤖 [THOUGHT] Creating study plan for {subject}...")
    
    messages = [
        {"role": "system", "content": "You are a strict but encouraging study tutor. Use tools to calculate study time, then output a structured plan."},
        {"role": "user", "content": f"Subject: {subject}\nDays until exam: {days_until_exam}\nCurrent level: {level}"}
    ]
    
    # Step 1: Tool Calling
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        tools=[study_tool],
        tool_choice="auto"
    )
    
    msg = response.choices[0].message
    if msg.tool_calls:
        messages.append(msg)
        for tool_call in msg.tool_calls:
            args = json.loads(tool_call.function.arguments)
            hours = calculate_study_hours(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": json.dumps({"recommended_hours": hours})
            })
            
    # Step 2: Structured Output
    schema = StudyPlan.model_json_schema()
    
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "study_plan_schema",
                "strict": True,
                "schema": schema
            }
        },
        temperature=0.2
    )
    
    result_json = response.choices[0].message.content
    return StudyPlan(**json.loads(result_json))

# ==========================================
# 4. Interactive CLI Loop
# ==========================================
def interactive_quiz_loop(plan: StudyPlan):
    """Administer the quiz and grade it interactively."""
    client = get_client()
    print("\n📝 [INTERACTIVE] Time for your Diagnostic Quiz!")
    print("=" * 50)
    
    score = 0
    for i, q in enumerate(plan.diagnostic_quiz):
        print(f"\nQuestion {i+1}: {q.question}")
        for opt in q.options:
            print(f"  {opt}")
            
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        # Use LLM to provide feedback
        messages = [
            {"role": "system", "content": "You are an encouraging tutor. Grade the student's answer and explain why it's right or wrong in 1-2 sentences."},
            {"role": "user", "content": f"Question: {q.question}\nCorrect Answer: {q.correct_answer}\nStudent Answer: {user_answer}"}
        ]
        
        feedback_response = client.chat.completions.create(
            model=get_model(),
            messages=messages,
            temperature=0.3
        )
        
        feedback = feedback_response.choices[0].message.content
        print(f"\n🤖 Tutor: {feedback}")
        
        if user_answer == q.correct_answer:
            score += 1
            
    print("=" * 50)
    print(f"🏆 Quiz Complete! Score: {score}/{len(plan.diagnostic_quiz)}")

def run():
    print("🚀 [PLANNING] Starting Study Planner Agent...")
    print("Please provide some details for your custom study plan.")
    
    subject = input("Subject to study (e.g., AWS Certified Developer, Python basics): ")
    days = input("Days until exam (e.g., 30): ")
    level = input("Current knowledge level (Beginner/Intermediate/Advanced): ")
    
    try:
        days = int(days)
    except:
        days = 30
        print("Invalid days. Defaulting to 30.")

    plan = generate_study_plan(subject, days, level)
    
    print("\n✅ [OUTPUT] Your Custom Study Plan:")
    print("=" * 50)
    print(f"⏱️ Total Recommended Study Hours: {plan.total_hours_recommended} hours")
    
    print("\n📅 Weekly Schedule:")
    for w in plan.weekly_schedule:
        print(f"  - {w}")
        
    print("\n📚 Recommended Resources:")
    for r in plan.recommended_resources:
        print(f"  - {r}")
    print("=" * 50)
    
    interactive_quiz_loop(plan)

if __name__ == "__main__":
    run()
