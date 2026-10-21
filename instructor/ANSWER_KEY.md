# Answer Key

## Exercise 1
**Q:** Why do we use the OpenAI SDK for Gemini here?
**A:** It provides a standardized interface for function calling and structured outputs that many agent frameworks (like AutoGen, CrewAI) rely on.

## Exercise 2
**Q:** What happens if `strict: True` is not supported or set?
**A:** The model might output Markdown formatting (```json ... ```) which breaks standard JSON parsers unless cleaned.

## Exercise 3
**Q:** Where should the agent's persona be defined?
**A:** In the `system` role message at the start of the messages array.

## Exercise 4
**Q:** How does the agent know the result of a tool?
**A:** We append a message with `role: "tool"`, `tool_call_id: <id>`, and `content: <result string>`.

## Exercise 5
**Q:** Why not put all memory in the context window?
**A:** Context window limits and cost. Persistent storage allows long-term, cross-session recall.
