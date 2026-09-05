#𝐂𝐨𝐧𝐭𝐞𝐱𝐭𝐒𝐡𝐢𝐟𝐭 — 𝐀𝐈-𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐂𝐨𝐧𝐭𝐞𝐱𝐭-𝐀𝐰𝐚𝐫𝐞 𝐖𝐨𝐫𝐤𝐬𝐩𝐚𝐜𝐞 𝐒𝐰𝐢𝐭𝐜𝐡𝐞𝐫

#𝐏𝐫𝐨𝐛𝐥𝐞𝐦 & 𝐆𝐨𝐚𝐥
Switching between work, study, and personal relaxation requires tedious manual setup—opening relevant tabs, filtering distraction sites, and reprioritizing tasks. This constant context switching leads to severe cognitive load and lost productivity.

ContextShift solves this for knowledge workers, students, and developers by functioning as an intelligent workspace orchestrator. Using lightweight AI reasoning, it transforms raw, unstructured session notes into a clean, 3-bullet execution plan while automatically configuring the browser environment. The goal is to eliminate digital friction, save at least 10–15 minutes of manual setup per transition, and help users instantly enter a flow state.

#𝐊𝐞𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬
Dynamic Workspace Orchestration: Automatically opens essential, context-specific browser URLs and resources based on selected modes (Work, Study, Personal).
AI Task Prioritization: Ingests raw, unstructured text notes and converts them into a sharp, prioritized 3-bullet action plan for the session.
Mindset Alignment: Generates short, real-time motivational prompts tailored to the user's focus target.

#𝐒𝐲𝐬𝐭𝐞𝐦 𝐀𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞

  <img width="314" height="712" alt="image" src="https://github.com/user-attachments/assets/c3d06e6e-e954-4b95-9467-0c7737582002" />


The system operates through a lightweight client-server architecture:

Frontend: The Chrome Extension (Manifest V3) captures the user's selected mode and raw session goals, then dispatches an asynchronous HTTP request.

Backend: A FastAPI server validates the incoming data, constructs a structured prompt, and queries the LLM engine.

Model: The LLM processes the input and returns structured JSON containing prioritized tasks, suggested URLs, and a mindset quote.

Execution: The backend forwards the JSON back to the Chrome extension, which dynamically renders the task list and triggers Chrome API tab creation (chrome.tabs.create) to set up the browser environment automatically.

#𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝
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

#𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐃𝐞𝐦𝐨
Project Demo URL (Optional): 
(https://docs.google.com/presentation/d/1lOHwKBV_OcjjxTgaV_TFew3ZRpZr0-Dxb_wKa-eXk_0/edit?slide=id.p1#slide=id.p1)

Evaluation Video: [Link to your 3-minute hackathon demo video]

#𝐋𝐢𝐦𝐢𝐭𝐚𝐭𝐢𝐨𝐧𝐬 & 𝐅𝐮𝐭𝐮𝐫𝐞 𝐖𝐨𝐫𝐤
Current Limitations:Currently opens new tabs alongside existing ones rather than isolating them into distinct Chrome Tab Groups.Backend needs to be running locally (localhost:8000) during evaluation.
Unfinished Features:Auto-closing or hiding distracting tabs (e.g., social media) during focus sessions.Local storage history for tracking completed tasks over time.
Future Roadmap:Native Chrome Tab Grouping & Window isolation per context.Integration with calendar APIs (Google Calendar/Notion) for automated scheduling transitions.On-device local LLM execution (e.g., WebLLM) for enhanced offline privacy.

#𝐓𝐡𝐢𝐫𝐝-𝐏𝐚𝐫𝐭𝐲 𝐒𝐞𝐫𝐯𝐢𝐜𝐞𝐬, 𝐃𝐚𝐭𝐚 & 𝐀𝐬𝐬𝐞𝐭𝐬
OpenAI API / Google Gemini API: Used for natural language inference and task prioritization. 
OpenAI Terms of UseFastAPI Framework: Open-source Web Framework under the MIT License. 
FastAPI GitHubChrome Extension API Documentation: Standard developer APIs provided by Google Chrome. 
Chrome DevelopersNote: No private keys, API tokens, or personal identifiers are committed to this repository. All credentials are read from local environment variables.

#𝐓𝐞𝐚𝐦 𝐌𝐞𝐦𝐛𝐞𝐫 𝐌𝐢𝐜𝐡𝐚𝐞𝐥

#𝐋𝐢𝐜𝐞𝐧𝐬𝐞 𝐍𝐎𝐍𝐄
