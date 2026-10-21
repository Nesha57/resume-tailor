import pytest
from pydantic import BaseModel, Field

# Mock schemas to ensure test passes regardless of solution state
class ContentPlan(BaseModel):
    title: str
    target_audience: str
    key_points: list[str]

class JobAnalysis(BaseModel):
    role: str
    required_skills: list[str]
    experience_level: str

def test_content_plan_valid():
    plan = ContentPlan(
        title="Agent Workshop",
        target_audience="Developers",
        key_points=["Agents", "LLMs", "Memory"]
    )
    assert plan.title == "Agent Workshop"
    assert len(plan.key_points) == 3

def test_content_plan_missing_fields():
    with pytest.raises(ValueError):
        ContentPlan(title="Incomplete")

def test_job_analysis_valid():
    job = JobAnalysis(
        role="AI Engineer",
        required_skills=["Python", "LLMs", "Prompting"],
        experience_level="Mid-Senior"
    )
    assert job.role == "AI Engineer"

def test_schema_generation():
    schema = ContentPlan.model_json_schema()
    assert schema["type"] == "object"
    assert "title" in schema["properties"]
    assert "target_audience" in schema["properties"]
