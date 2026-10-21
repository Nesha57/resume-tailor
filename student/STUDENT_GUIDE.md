# Student Guide: AI Agent Workshop (Day 2)

Welcome to Day 2 of the AI Agent Workshop! Today, we transition from theory to practice. You will build intelligent, tool-using AI agents from scratch using Python and the Google Gemini API.

## Workshop Goals
By the end of today, you will be able to:
1. Understand the core ReAct (Reason + Act) loop that powers AI agents.
2. Build applications that interact with the Gemini API via the OpenAI SDK compatibility layer.
3. Equip LLMs with custom Python tools (functions).
4. Enforce strict JSON data structures for reliable application integration.
5. Design multi-tool, problem-solving agents.

## Schedule Outline
- **Morning Session (9:00 AM - 12:00 PM)**
  - Environment Setup & API Verification
  - Exercise 1 & 2: Basic API Calls and Structured Outputs
  - Exercise 3: Intro to Tool Calling
- **Lunch (12:00 PM - 1:00 PM)**
- **Afternoon Session (1:00 PM - 4:00 PM)**
  - Exercise 4 & 5: The Agent Loop and State Management
  - Exercise 6 & 7: Multi-tool Agents
  - Capstone Design Activity: Agent Design Canvas
- **Wrap-up (4:00 PM - 5:00 PM)**
  - Review, Q&A, and Next Steps

## 1. Setup Instructions

Please follow the detailed setup instructions in `docs/setup.md`. The high-level steps are:
1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Install requirements (`pip install openai python-dotenv pydantic pytest`).
4. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com).
5. Create a `.env` file with `GEMINI_API_KEY` and `GEMINI_MODEL=gemini-2.5-flash`.
6. Run `python verify_setup.py`.

## 2. Running the Exercises

The workshop consists of several hands-on exercises located in the `src/` directory (or wherever your instructor has placed them).

Each exercise typically has two parts:
- `starter/`: Contains incomplete code with `TODO` comments. This is where you will write your code!
- `solution/`: Contains the complete, working code for reference. Try not to look at this until you've attempted the starter code!

### How to run an exercise:
Always run the scripts from the root of your project directory so the `.env` file is loaded correctly.

```bash
# Example: Running Exercise 1 starter code
python path/to/exercise1/starter/main.py
```

## 3. Important Tips for Success
- **Read the `TODO`s:** The starter code files are heavily commented with exact instructions on what to implement.
- **Use the Docs:** Refer to `docs/concepts.md` if you get stuck on the theory.
- **Check your formatting:** When working with LLMs, the exact structure of JSON schemas and messages arrays is critical. One misplaced bracket will cause API errors.
- **Troubleshooting:** If you hit an error, check `docs/troubleshooting.md` first!
- **Have fun!** Don't be afraid to experiment and change the prompts or tools.

## 4. The Agent Design Canvas

During the afternoon session, we will use the `AGENT_DESIGN_CANVAS.md` to plan a custom agent. This is a critical step in translating real-world problems into agent architecture before writing a single line of code.
