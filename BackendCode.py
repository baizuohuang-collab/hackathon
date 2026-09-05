import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai  # or google-generativeai

app = FastAPI(title="ContextShift API")

# Enable CORS for Chrome Extension requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

class ModeRequest(BaseModel):
    mode: str  # "Work", "Study", or "Personal"
    raw_notes: str

@app.post("/api/shift-context")
async def shift_context(data: ModeRequest):
    try:
        prompt = f"""
        You are ContextShift AI. The user is transitioning to '{data.mode}' mode.
        Based on their raw notes: "{data.raw_notes}", provide a JSON response with:
        1. "top_3_tasks": An array of 3 clear, actionable tasks for this focus session.
        2. "suggested_urls": An array of up to 3 useful search/web URLs for this context (e.g., https://google.com, https://github.com).
        3. "focus_quote": A short 1-sentence motivational micro-quote.

        Return strictly valid JSON without markdown formatting.
        """

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        import json
        result = json.loads(response.choices[0].message.content)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
