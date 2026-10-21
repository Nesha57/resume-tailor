# Day 2 Instructor Guide: Advanced AI Agents with Gemini API

Welcome to Day 2! This guide will walk you through leading the workshop.

## Learning Objectives
- Master the Gemini API using the OpenAI SDK compatibility layer.
- Understand tool calling (function calling) natively with Gemini.
- Implement structured JSON outputs using Pydantic schemas.
- Build persistent memory patterns for agents.
- Orchestrate multi-agent systems and loops.

## Exercise 1: Setup and Basic Chat
- **Time:** 30 min
- **Demonstrate:** How to set `GEMINI_API_KEY` and initialize the OpenAI client with Gemini's base URL.
- **Common Mistakes:** Forgetting `base_url` in client setup.
- **Checkpoint Question:** Why do we use the OpenAI SDK for Gemini here?
  - *Answer:* For cross-compatibility and standard tool calling abstractions.

## Exercise 2: Structured Outputs
- **Time:** 45 min
- **Demonstrate:** Passing `response_format` with a JSON schema generated from Pydantic.
- **Checkpoint Question:** What happens if `strict: True` is not supported or set?
  - *Answer:* The LLM might output extra text or Markdown formatting around the JSON.

## Exercise 3: Prompt Engineering for Agents
- **Time:** 30 min
- **Demonstrate:** System instructions vs user instructions.
- **Checkpoint Question:** Where should the agent's persona be defined?
  - *Answer:* In the system prompt.

## Exercise 4: Tool Calling
- **Time:** 60 min
- **Demonstrate:** Creating a tool schema and processing `tool_calls` in the response.
- **Common Mistakes:** Not appending the tool response back to the message history.
- **Checkpoint Question:** How does the agent know the result of a tool?
  - *Answer:* We append a `tool` role message with the result.

## Exercise 5: Memory and State
- **Time:** 45 min
- **Demonstrate:** Saving facts to a JSON file.
- **Checkpoint Question:** Why not put all memory in the context window?
  - *Answer:* Context windows are limited and cost money per token; persistent storage allows long-term recall.

## Exercise 6: Multi-Agent Architectures
- **Time:** 60 min
- **Demonstrate:** Passing output from a Researcher agent to a Writer agent.

## Exercise 7: Final Project
- **Time:** 90 min
- **Demonstrate:** Tying it all together.

## Troubleshooting
Refer to `TROUBLESHOOTING.md`.
