# Exercise 02: Prompt Engineering & Behavioral Steering Engine

## Overview
Now that we can talk to the LLM, let's learn how to steer its behavior effectively. Good prompt engineering is the difference between a generic, unhelpful response and a highly specialized, expert outcome.

## 5 Core Prompt Components
A robust enterprise prompt should contain these 5 components:
1. **Role**: Who is the AI acting as? (e.g., "Senior Python Developer")
2. **Objective**: What is the specific goal?
3. **Context**: Background information needed to succeed.
4. **Constraints**: Rules the AI must follow (e.g., "Do not use external libraries").
5. **Format**: How the output should be structured (e.g., Markdown, JSON).

## The Progression: BAD vs GOOD
- **BAD**: "Help me write a resume."
- **GOOD**: "Act as an expert Tech Recruiter (Role). Review the following bullet points and improve them to highlight impact and metrics (Objective). The candidate is applying for a Senior Data Scientist role at a FAANG company (Context). Do not make up fake metrics; use placeholders like [X] if needed (Constraints). Provide the output as a Markdown list of revised bullet points with a brief explanation of why the change was made (Format)."

## Exercise Steps
1. Review `starter.py` and implement the 5 prompt frameworks.
2. Observe how the LLM's response changes based on the persona and constraints.
