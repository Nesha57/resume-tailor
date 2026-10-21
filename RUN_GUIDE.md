# Runner Guide

Follow these steps to set up your environment and run the exercises.

## Step 1: Python Environment Setup

It is highly recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## Step 2: Gemini API Key Configuration

1. Visit [Google AI Studio](https://aistudio.google.com) and sign in.
2. Create a new API key. It's free!
3. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Open `.env` and set your key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   ```

## Step 3: Running Exercises

Each exercise has a `starter.py` in the `day2/` directory and a `solution.py` in the `solutions/` directory.

### Example: Exercise 1

**Run Starter:**
```bash
python day2/01_first_llm_call/starter.py
```
*(If it's incomplete, you will see TODOs in the file.)*

**Run Solution:**
```bash
python solutions/01_first_llm_call/solution.py
```
*Expected Output:* You should see a professional terminal UI with emojis, logging the `[PLANNING]`, `[OUTPUT]`, etc., demonstrating a successful call to the Gemini API.

## Step 4: Running Unit Tests

To verify solutions, run the test suite using `pytest`. Note: Some tests might be mocked, while others might require the API key.

```bash
pytest tests/
```

## Step 5: Troubleshooting

- **Error: GEMINI_API_KEY not found in environment variables.**
  Make sure you created the `.env` file and it is located in the root directory where you are running the script. Ensure `python-dotenv` is installed.
- **ModuleNotFoundError: No module named 'openai'**
  Ensure your virtual environment is activated and you ran `pip install -r requirements.txt`.
- **401 Unauthorized or Invalid API Key**
  Check that you copied the full API key from Google AI Studio without extra spaces.
