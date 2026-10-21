# Workshop Setup Guide

Welcome to the AI Agent Workshop! Before we dive into building agents, we need to set up your development environment. This guide will walk you through installing Python, setting up a virtual environment, installing dependencies, and configuring your API key for Google's Gemini.

## 1. Prerequisites

You will need **Python 3.10 or higher** installed on your system.

### Windows
1. Download the Python installer from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer.
3. **CRITICAL**: Check the box that says **"Add Python to PATH"** at the bottom of the installer window before clicking "Install Now".
4. Verify installation by opening PowerShell and typing:
   ```powershell
   python --version
   ```

### macOS
1. We recommend using Homebrew. If you don't have it, install it from [brew.sh](https://brew.sh/).
2. Run:
   ```bash
   brew install python
   ```
3. Verify installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)
1. Run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```
2. Verify installation:
   ```bash
   python3 --version
   ```

---

## 2. Setting Up Your Project

We will use a Python virtual environment to keep our project dependencies isolated.

### Step 2.1: Open your terminal and navigate to the project directory
```bash
cd path/to/ai-agent-workshop-day2
```

### Step 2.2: Create a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

### Step 2.3: Activate the virtual environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
*(Note: If you get a Script Execution Policy error, run `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` as administrator and try again.)*

**macOS/Linux:**
```bash
source venv/bin/activate
```
*(You should now see `(venv)` at the beginning of your terminal prompt.)*

---

## 3. Install Dependencies

With your virtual environment active, install the required packages:

```bash
pip install --upgrade pip
pip install openai python-dotenv pydantic pytest
```

*Note: We are using the `openai` Python package because the Gemini API offers full OpenAI SDK compatibility!*

---

## 4. Get a Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on **"Get API key"** in the left navigation menu.
4. Click **"Create API key"** and choose to create a key in a new project.
5. Copy your new API key.

---

## 5. Configure Your Environment Variables

1. In the root of your project directory, copy the `.env.example` file to `.env`:
   - Windows: `copy .env.example .env`
   - Mac/Linux: `cp .env.example .env`
2. Open the `.env` file in your code editor.
3. Add your Gemini API key and set the model:

```ini
GEMINI_API_KEY=your_copied_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

---

## 6. Verify Your Setup

Let's test if everything is working correctly. Create a file named `verify_setup.py` in the root of your project with the following code:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in environment variables.")
        return

    print("✅ API Key found in .env file.")
    print("⏳ Connecting to Gemini API...")

    try:
        # Initialize the client using OpenAI compatibility layer
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        
        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "Say 'Hello from Gemini!' and nothing else."}
            ]
        )
        
        reply = response.choices[0].message.content
        print(f"✅ Connection successful! Model says: {reply}")
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")

if __name__ == "__main__":
    main()
```

Run the script:
```bash
python verify_setup.py
```

If you see **"✅ Connection successful! Model says: Hello from Gemini!"**, you are ready for the workshop!
