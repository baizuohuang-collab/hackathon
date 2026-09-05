#ContextShift — AI-Powered Context-Aware Workspace Switcher

#Problem & Goal
Switching between work, study, and personal relaxation requires tedious manual setup—opening relevant tabs, filtering distraction sites, and reprioritizing tasks. This constant context switching leads to severe cognitive load and lost productivity.

ContextShift solves this for knowledge workers, students, and developers by functioning as an intelligent workspace orchestrator. Using lightweight AI reasoning, it transforms raw, unstructured session notes into a clean, 3-bullet execution plan while automatically configuring the browser environment. The goal is to eliminate digital friction, save at least 10–15 minutes of manual setup per transition, and help users instantly enter a flow state.

#Key Features
Dynamic Workspace Orchestration: Automatically opens essential, context-specific browser URLs and resources based on selected modes (Work, Study, Personal).
AI Task Prioritization: Ingests raw, unstructured text notes and converts them into a sharp, prioritized 3-bullet action plan for the session.
Mindset Alignment: Generates short, real-time motivational prompts tailored to the user's focus target.

#System Architecture
+-------------------------------------------------------------+
|               Chrome Extension (Frontend)                   |
|  [popup.html] <--User Input-- [popup.js / Manifest V3]      |
+------------------------------+------------------------------+
                               |
                        HTTP POST Request
                        (JSON Payload)
                               v
+-------------------------------------------------------------+
|                     FastAPI (Backend)                       |
|   - CORS Middleware & Request Validation                    |
|   - Prompt Formatting & Schema Normalization                |
+------------------------------+------------------------------+
                               |
                       Async REST API Call
                               v
+-------------------------------------------------------------+
|                      External AI Model                      |
|                   (OpenAI / Gemini LLM)                     |
+-------------------------------------------------------------+

The system operates through a lightweight client-server architecture:

Frontend: The Chrome Extension (Manifest V3) captures the user's selected mode and raw session goals, then dispatches an asynchronous HTTP request.

Backend: A FastAPI server validates the incoming data, constructs a structured prompt, and queries the LLM engine.

Model: The LLM processes the input and returns structured JSON containing prioritized tasks, suggested URLs, and a mindset quote.

Execution: The backend forwards the JSON back to the Chrome extension, which dynamically renders the task list and triggers Chrome API tab creation (chrome.tabs.create) to set up the browser environment automatically.

#Technologies Used
AI Model    OpenAI GPT-4o-mini / Gemini APINatural language understanding, task extraction, and URL inference
Frontend    HTML5, CSS3, JavaScript (Chrome Manifest V3)User interface and browser automation via Chrome Extension APIs
Backend    Python, FastAPI, UvicornAPI routing, request validation, and AI integration orchestration
Sponsor Tech    OpenAI API / Google Gemini APICore AI inference provider

#Installation & Execution
# 1. Clone the repository
git clone https://github.com/your-username/context-shift.git
cd context-shift

# 2. Set up and start the Backend
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required packages
pip install fastapi uvicorn openai pydantic

# Set your API Key
export OPENAI_API_KEY="your_actual_api_key_here"  # On Windows PowerShell: $env:OPENAI_API_KEY="your_actual_api_key_here"

# Launch the FastAPI server
python main.py
# Server will run at http://localhost:8000

# 3. Load the Chrome Extension Frontend
# - Open Google Chrome and navigate to chrome://extensions/
# - Enable "Developer mode" via the toggle in the top-right corner.
# - Click "Load unpacked" and select the `frontend/` directory from this repository.
# - Click the ContextShift extension icon in your toolbar to begin.

#Project Demo
Project Demo URL (Optional): N/A (Local Extension Demo)
Evaluation Video: [Link to your 3-minute hackathon demo video]

#Limitations & Future Work
Current Limitations:Currently opens new tabs alongside existing ones rather than isolating them into distinct Chrome Tab Groups.Backend needs to be running locally (localhost:8000) during evaluation.
Unfinished Features:Auto-closing or hiding distracting tabs (e.g., social media) during focus sessions.Local storage history for tracking completed tasks over time.
Future Roadmap:Native Chrome Tab Grouping & Window isolation per context.Integration with calendar APIs (Google Calendar/Notion) for automated scheduling transitions.On-device local LLM execution (e.g., WebLLM) for enhanced offline privacy.

#Third-Party Services, Data & AssetsOpenAI API / Google Gemini API: Used for natural language inference and task prioritization. 
OpenAI Terms of UseFastAPI Framework: Open-source Web Framework under the MIT License. 
FastAPI GitHubChrome Extension API Documentation: Standard developer APIs provided by Google Chrome. 
Chrome DevelopersNote: No private keys, API tokens, or personal identifiers are committed to this repository. All credentials are read from local environment variables.

#Team Member Michael 

#License NONE
