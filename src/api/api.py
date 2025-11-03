from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
try:
    from agent.src.agent.crew import ResearchCrew
    
except ImportError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from agent.src.agent.crew import ResearchCrew
import os
from pathlib import Path

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))
static_dir = os.path.join(base_dir, "static")
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "output")

app = FastAPI()

# Mount static files directory
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

class KickoffRequest(BaseModel):
    topic: str

@app.get("/", response_class=HTMLResponse)
async def agent_config(request: Request):
    """Home endpoint with research assistant information"""
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
    
@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy",
        "message": "API is running"
    }

@app.post("/kickoff")
def kickoff(request: KickoffRequest):
    """
    Kickoff the research crew with the provided topic.
    """
    try:
        inputs = {
            'topic': request.topic
        }
        research_crew = ResearchCrew()
        result = research_crew.crew().kickoff(inputs=inputs)
        return {
            "status": "success",
            "topic": request.topic,
            "result": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running crew: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)