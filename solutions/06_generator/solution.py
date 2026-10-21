import os
import sys
import json
from typing import List
from pydantic import BaseModel, Field
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

class ContentPlan(BaseModel):
    title: str = Field(description="The catchy title of the article")
    executive_summary: str = Field(description="A 2-3 sentence summary of the article's core message")
    target_audience: str = Field(description="Who this article is written for")
    section_breakdown: List[str] = Field(description="List of section headings/topics")
    quality_checks: List[str] = Field(description="List of specific things to verify before publishing (e.g. 'Check for clear code examples')")
    seo_keywords: List[str] = Field(description="List of 3-5 SEO keywords to target")
    call_to_action: str = Field(description="The final action we want the reader to take")
    read_time: int = Field(description="Estimated read time in minutes")

def generate_content_plan(topic: str):
    print(f"\n📝 Generating Content Plan for: '{topic}'...\n")
    
    # 1. Get the JSON schema representation from Pydantic
    schema = ContentPlan.model_json_schema()
    
    messages = [
        {"role": "system", "content": "You are an expert Content Architect. Create comprehensive content plans based on the provided topic."},
        {"role": "user", "content": f"Create a detailed content plan for a blog post about: {topic}"}
    ]
    
    # 2. Call the API, forcing the output to strictly match our schema
    response = get_client().chat.completions.create(
        model=get_model(),
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "content_plan_schema",
                "strict": True,
                "schema": schema
            }
        }
    )
    
    raw_json = response.choices[0].message.content
    
    # 3. Parse the raw JSON back into our Pydantic model for validation and easy access
    try:
        plan = ContentPlan.model_validate_json(raw_json)
        
        # 4. Render a nice CLI report
        print(f"==================================================")
        print(f"📊 CONTENT PLAN: {plan.title}")
        print(f"⏱️  Est. Read Time: {plan.read_time} min")
        print(f"🎯 Target Audience: {plan.target_audience}")
        print(f"==================================================\n")
        
        print("📝 Executive Summary:")
        print(f"{plan.executive_summary}\n")
        
        print("📑 Section Breakdown:")
        for idx, section in enumerate(plan.section_breakdown, 1):
            print(f"  {idx}. {section}")
        print()
        
        print("🔑 SEO Keywords:")
        print(f"  {', '.join(plan.seo_keywords)}\n")
        
        print("✅ Quality Checks:")
        for check in plan.quality_checks:
            print(f"  - {check}")
        print()
        
        print("📣 Call to Action:")
        print(f"  {plan.call_to_action}")
        print(f"==================================================\n")
        
    except Exception as e:
        print(f"❌ Failed to parse response: {e}")
        print(f"Raw Output: {raw_json}")


if __name__ == "__main__":
    generate_content_plan("How AI Agents Will Transform Software Engineering in 2026")
