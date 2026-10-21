# Frequently Asked Questions (FAQ)

## 1. Why are we using the OpenAI Python package for Google's Gemini?
Google Gemini offers a fully compatible OpenAI API endpoint. This means you can use the familiar, industry-standard `openai` Python SDK (which is widely supported by agent frameworks and tools) while leveraging the power, massive context window, and speed of Gemini models. It's the best of both worlds!

## 2. Is the Gemini API free?
Google AI Studio offers a very generous free tier that is more than sufficient for this workshop and most personal projects. Note that data sent via the free tier may be used to train Google's models. Paid tiers (via Google Cloud Vertex AI) offer enterprise data privacy.

## 3. What is the difference between `gemini-2.5-flash` and `gemini-2.5-pro`?
- **Flash:** Extremely fast, cost-effective, and highly capable for most agentic tasks, tool calling, and general reasoning. It is the default for this workshop.
- **Pro:** Heavier, slightly slower, but capable of more complex reasoning, coding tasks, and handling very intricate prompts. Use it when Flash struggles.

## 4. Will the LLM steal my data?
If you use the free tier of Google AI Studio, your prompts and data may be logged and used to improve future models. Do not send sensitive personal information (PII) or proprietary company secrets through the free tier. Enterprise tiers (Vertex AI) do not use your data for training.

## 5. What is the difference between building agents with native Python code vs. frameworks like LangChain or AutoGen?
- **Native Code (Our Approach):** You write the loops, manage the state, and handle the API calls directly. It is transparent, easier to debug, and teaches you exactly how things work under the hood. It's often preferred for production.
- **Frameworks:** Provide higher-level abstractions and pre-built tools. They can be faster to prototype with but can become "black boxes" that are hard to debug when things go wrong.

## 6. How does the agent "know" what tools to use?
You provide a JSON schema describing available tools (name, description, required arguments) in every API request. The LLM reads these descriptions and, based on the user's prompt, decides if it should generate a JSON response requesting a tool call instead of generating regular text.

## 7. What is RAG and how does it relate to Agents?
Retrieval-Augmented Generation (RAG) is a technique where you search a database for relevant information and inject it into the prompt *before* sending it to the LLM. An Agent can use RAG as one of its tools (e.g., a "search_internal_docs" tool).

## 8. Can my agent execute terminal commands?
Yes, you can write a tool that uses Python's `subprocess` module to run terminal commands. **WARNING:** This is extremely dangerous. You should only run LLM-generated commands in secure, isolated sandboxes (like Docker containers), never on your host machine.

## 9. How do I stop an agent that's stuck in an infinite loop?
Press `Ctrl+C` in your terminal to interrupt the Python script. To prevent this in code, implement a `max_iterations` counter in your agent loop (e.g., force it to stop after 10 tool calls).

## 10. Why did the LLM generate invalid JSON?
While modern models like Gemini are great at outputting JSON, they aren't perfect. They might append text like "Here is your JSON:" or miss a comma. Using Structured Outputs (JSON Schema mode) forces the model to adhere strictly to the format, eliminating these errors.

## 11. Can agents run asynchronously?
Yes! In production, you would use `asyncio` and the `AsyncOpenAI` client to run multiple agent tasks concurrently without blocking your main application thread.

## 12. How large is the context window for Gemini?
Gemini 1.5 and 2.0 models have massive context windows, up to 1 million or even 2 million tokens. This means you can pass entire books, codebases, or hours of video directly into the prompt!

## 13. Does the LLM remember my previous questions?
No, the API is completely stateless. To have a conversation, your application must store the history (e.g., in a list) and send the *entire* history back to the API with every new message.

## 14. What are tokens?
Tokens are the basic units of text processed by an LLM. A token is typically about 4 characters or 3/4 of a word in English. API costs and limits are calculated based on token counts.

## 15. How do I deploy my agent?
You can deploy your Python agent as a web server using frameworks like FastAPI or Flask, package it in a Docker container, and host it on cloud platforms like Google Cloud Run, AWS Fargate, or Heroku.
