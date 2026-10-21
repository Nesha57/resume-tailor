# AI Agent Design Canvas

Use this canvas to design your custom AI agent before writing code. 

## 1. Core Identity
- **Agent Name:** 
- **Core Purpose (1 sentence):** 

## 2. The Problem Space
- **What specific problem does this agent solve?** 
- **Who is the end user?** 
- **What does the user provide as input?** 

## 3. The LLM Configuration
- **Model:** (e.g., gemini-2.5-flash)
- **System Prompt (Draft):**
  > You are a [Role]. Your job is to [Task]. You must always [Constraint].

## 4. Tools (Actions)
List the specific functions the agent needs to interact with the world.

| Tool Name | Description (For the LLM) | Inputs Required | Output Provided |
| :--- | :--- | :--- | :--- |
| `search_db` | Searches the internal product database | `query` (str) | JSON list of products |
| | | | |
| | | | |

## 5. Memory & Knowledge
- **Short-term Memory:** What context needs to be passed in the active conversation window? (e.g., Last 10 messages, current order ID).
- **Long-term Knowledge:** What external data sources does it need to access? (e.g., PDF manuals, live API data).

## 6. Output & Handoff
- **What is the final structured output expected from the agent?** (e.g., A JSON summary, a formatted email).
- **Stop Condition:** How does the agent know it is finished with the task?
- **Failure State:** What should the agent do if a tool fails or it gets confused?
