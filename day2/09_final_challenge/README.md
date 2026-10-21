# Exercise 09: Final Challenge & Capstone Engine

Welcome to the Final Challenge! You will design and implement a custom agent from scratch.

## Agent Design Canvas (15 Minutes)
Before writing code, sketch out your agent:
1. **Persona & Goal**: Who is the agent, and what does it achieve?
2. **Inputs (Context)**: What files, prompts, or dynamic context will it ingest?
3. **Tools (Actions)**: What real-world actions or lookups does it need (e.g., API calls, DB queries, calculators)?
4. **Structured Outputs**: What does the final output schema look like?

## The Challenge
Implement an **Autonomous Study Planner & Exam Prep Agent**.

### Requirements
- **Persona**: A strict but encouraging study tutor.
- **Inputs**: User's subject, time until exam, and current knowledge level.
- **Tools**: Give the agent a tool to calculate how many hours per week they should study.
- **Structured Output**: Use Pydantic to enforce a schema that returns a weekly study schedule, recommended resources, and a 3-question diagnostic quiz.
- **Interactivity**: Add a simple CLI loop where the user can answer the quiz questions and get feedback from the agent.

## Instructions
- Start with `starter.py` and build your solution.
- Use everything you've learned: Setup client, Tool calling, Structured Output, Interactive Context Loop.
- Check `solutions/09_final_challenge/solution.py` for a complete reference implementation.
