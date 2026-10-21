# Troubleshooting Guide

This guide covers common issues you might encounter during the workshop.

## 1. `python` or `python3` command not found
**Symptom:** Terminal says "command not found: python" or "Python is not recognized as an internal or external command".
**Cause:** Python is not installed, or not added to your system's PATH.
**Fix:** 
- Windows: Reinstall Python and check the "Add Python to PATH" box.
- Mac/Linux: Ensure you installed Python via Homebrew/apt. Try running `python3` instead of `python`.
**Trainer Explanation:** The OS doesn't know where the Python executable is located.

## 2. Virtual Environment Won't Activate (Windows)
**Symptom:** `.\venv\Scripts\Activate.ps1` gives an Execution Policy error.
**Cause:** Windows PowerShell restricts running scripts by default for security.
**Fix:** Run PowerShell as Administrator and execute: `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`. Then try activating again.
**Trainer Explanation:** PowerShell blocks script execution (like the activate script) by default on Windows.

## 3. ModuleNotFoundError: No module named 'openai'
**Symptom:** Script crashes on `import openai` or similar.
**Cause:** Dependencies aren't installed, or you installed them outside the active virtual environment.
**Fix:** 
1. Ensure your terminal prompt shows `(venv)`. If not, activate it.
2. Run `pip install -r requirements.txt` or `pip install openai python-dotenv pydantic pytest`.
**Trainer Explanation:** Pip installs packages globally if a venv isn't active. The script is looking in the venv (which is empty) or vice-versa.

## 4. GEMINI_API_KEY is missing or invalid
**Symptom:** API returns an AuthenticationError (401/403) or the script complains about a missing key.
**Cause:** Your `.env` file is missing, misnamed (e.g., `.env.txt`), or the key is wrong.
**Fix:** Ensure you have a file named exactly `.env` (no extension) in the root of your project, containing `GEMINI_API_KEY=your_key`. Make sure you are using `load_dotenv()` in your code.
**Trainer Explanation:** The code needs the API key to authenticate with Google's servers.

## 5. RateLimitError (429)
**Symptom:** "Too Many Requests" or "Quota Exceeded".
**Cause:** You are hitting the API too fast or have exceeded your free tier quota on Google AI Studio.
**Fix:** Wait a minute and try again. For continuous issues, you may need to add billing to your Google Cloud project (though the free tier is usually sufficient for this workshop).
**Trainer Explanation:** APIs have limits on how many requests you can make per minute to prevent abuse.

## 6. Invalid JSON Response / JSONDecodeError
**Symptom:** Code crashes trying to parse the LLM's output with `json.loads()`.
**Cause:** The LLM outputted text along with the JSON (e.g., markdown code blocks like \`\`\`json), or invalid JSON.
**Fix:** Use the `response_format={"type": "json_schema", ...}` feature of the API to guarantee valid JSON, or write a robust parsing function that strips markdown backticks.
**Trainer Explanation:** LLMs are text generators. Without strict constraints, they like to be helpful and chatty, wrapping data in conversational text.

## 7. Pydantic ValidationError
**Symptom:** Pydantic raises an error like "field required" or "value is not a valid integer".
**Cause:** The LLM's JSON output didn't perfectly match your Pydantic model's schema.
**Fix:** Ensure your schema descriptions are clear. Use strict JSON schemas in the API request. 
**Trainer Explanation:** Pydantic is enforcing strict types. If the LLM returns a string "five" instead of the integer 5, Pydantic will fail.

## 8. Tool Call Request Fails to Parse
**Symptom:** The agent enters a loop or crashes trying to execute a tool.
**Cause:** The arguments returned by the LLM for the tool call are missing or formatted incorrectly.
**Fix:** Check the `description` fields in your tool definitions. The LLM relies heavily on these to know what data to provide.
**Trainer Explanation:** The LLM generates arguments based on the schema you provide. If the schema is ambiguous, the output will be wrong.

## 9. Infinite Agent Loop
**Symptom:** The agent keeps calling the same tool over and over with the same inputs.
**Cause:** The agent isn't getting the information it needs from the tool result, or the prompt isn't giving it a clear "Stop Condition".
**Fix:** Improve the tool result string format (make it clear and concise). Add instructions to the system prompt like "Once you have the answer, provide the final response to the user."
**Trainer Explanation:** Agents are just while loops. If the state doesn't change meaningfully after a tool call, the LLM will predict the exact same next action.

## 10. Max Tokens Reached (Incomplete Output)
**Symptom:** The LLM's response cuts off mid-sentence.
**Cause:** The response exceeded the `max_tokens` limit set in the API request, or the model's absolute output limit.
**Fix:** Increase `max_tokens` in your API call, or ask the LLM to be more concise.
**Trainer Explanation:** Outputting text is expensive. There is always a cap on how long a single response can be.

## 11. Context Window Exceeded
**Symptom:** API returns an error about exceeding the maximum context length.
**Cause:** Your prompt (including history and tool results) is too long.
**Fix:** Implement memory summarization, truncate history, or use a model with a larger context window (Gemini 1.5 Pro/Flash has a massive context window, so this is rare).
**Trainer Explanation:** Every model has a limit on how much text it can process at once.

## 12. Changes in Code aren't reflecting
**Symptom:** You modify the code, run it, and get the old behavior.
**Cause:** You forgot to save the file, or you are running a different script than you are editing.
**Fix:** Save the file (Ctrl+S / Cmd+S). Verify the file path in your terminal matches what you're editing.
**Trainer Explanation:** A common basic mistake when moving quickly.

## 13. dotenv is not loading variables
**Symptom:** `os.getenv("GEMINI_API_KEY")` returns `None` even though `.env` exists.
**Cause:** You are running the script from a different directory, so it can't find `.env` in the current working directory, or `load_dotenv()` wasn't called.
**Fix:** Make sure your terminal is in the project root directory when you run `python script.py`. Ensure `load_dotenv()` is at the top of your script.
**Trainer Explanation:** `load_dotenv` looks for the file in the directory where the command was executed, not necessarily where the script is located.
