# Assessment Rubric (20 Points Total)

| Criteria | 0-1 Points | 2-3 Points | 4-5 Points |
|----------|------------|------------|------------|
| **1. API Integration** | Fails to connect to Gemini API. | Connects but lacks robust error handling. | Clean initialization with SDK compatibility and error handling. |
| **2. Prompting & Persona** | Generic or weak system prompts. | Decent instructions but misses edge cases. | Strong, clear instructions preventing hallucinations. |
| **3. Tool Implementation** | Tools do not work or schema is malformed. | Tools work but parsing is brittle. | Tools perfectly integrated, robust error handling, correct history management. |
| **4. Architecture/State** | Hardcoded logic, no real state. | Basic memory loop. | Advanced state/memory management (e.g., JSON persistence). |
