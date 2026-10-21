# Exercise 04: Multi-Tool Agent Engine

## 🎯 Goal
Understand and implement a generic Tool Calling Agent Engine. You will learn the critical concept that **the LLM does NOT execute tools; it only suggests them**. Your application code executes the tool and feeds the result back to the LLM.

## 🏗️ Architecture

```mermaid
sequenceDiagram
    participant User
    participant App as Your App (Agent Loop)
    participant LLM as Gemini API
    participant Tools as Tools (Calc, Search, DB)

    User->>App: "Calculate total cost and look up policy"
    App->>LLM: Prompt + Conversation History + Tool Definitions
    LLM-->>App: Tool Call Request (e.g., `calculator`, `search`)
    App->>Tools: Execute function locally
    Tools-->>App: Result (e.g., "150.00", "Policy:...")
    App->>LLM: Tool Output + Previous History
    LLM-->>App: Final natural language response
    App-->>User: Formatted output
```

## 🛠️ Instructions
1. Open `day2/04_tool_calling/starter.py`.
2. Implement the missing tool implementations (`calculator`, `search_knowledge_base`, `get_user_profile`).
3. Define the JSON Schema for the tools.
4. Implement the Agent Loop to parse tool requests, execute them, and feed results back.
5. Run the code and observe the execution trace.

## 🤔 Checkpoint Questions
- What happens if the tool execution fails? How should the LLM know?
- Why do we need a maximum iteration limit on the tool calling loop?
- How does the model know what arguments to provide to a tool?
