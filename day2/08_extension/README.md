# Exercise 08: Extend the Agent

Welcome to Exercise 08! In this exercise, you will extend the base agent from Exercise 07 with five powerful enterprise extensions.

## Objective
Implement five distinct extensions to elevate the agent from a simple prompt wrapper to a robust, interactive system.

## The 5 Extensions
- **Option A: Salary Calculator Tool (Tool Calling)**: Give the agent a tool to estimate salary ranges based on role, location, and experience.
- **Option B: Persistent Candidate Memory (Conversation History)**: Allow the agent to remember context across multiple interactions in a CLI loop.
- **Option C: Multi-Stage Critic Loop**: Add a self-reflection step where the agent critiques its own analysis before returning the final result.
- **Option D: HR Policy RAG Engine**: Simulate a simplistic RAG retrieval step to pull in relevant HR policies (e.g., relocation, benefits).
- **Option E: Confidence & Self-Evaluation Scoring**: Update the output schema to include a `confidence_score` and a `reasoning` field for explainability.

## Instructions
1. Open `starter.py` and review the TODOs corresponding to Options A through E.
2. You can implement these extensions one by one or attempt all of them.
3. Use the knowledge gained from previous exercises (Tool calling, Context management, Structured Outputs).
4. Check the `solutions` folder if you get stuck.
