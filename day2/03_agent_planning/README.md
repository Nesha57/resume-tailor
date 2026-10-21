# Exercise 03: Autonomous Task Planner & Reasoning Loop

## Overview
Agents are more than just chatbots; they can plan, reason, and act. In this exercise, you'll build an `AutonomousTaskPlanner` that takes a high-level goal from a user and decomposes it into a structured, actionable plan.

## The Planning Concept
An autonomous agent typically operates in a loop:
1. **Understand Goal**: What is the final objective?
2. **Decompose**: Break the goal into chronological tasks.
3. **Assess Risks**: What could go wrong at each step?
4. **Determine Tools**: What tools (functions) are needed to accomplish the task?
5. **Define Success**: How do we know the plan worked?

## Structured Output
Instead of returning a free-form string, we will force the LLM to return data adhering to a specific JSON schema using the Gemini API's Structured Output capabilities (via the OpenAI SDK's `response_format`).

## Steps
1. Review `starter.py` and set up your Pydantic schemas.
2. Implement the `AutonomousTaskPlanner` class.
3. Provide a high-level goal (e.g., "Analyze the latest tech news and write a summary report") and generate a structured plan.
4. Run your code and observe the live CLI logging ([PLANNING], [THOUGHT], [TASK DECOMPOSITION]).
