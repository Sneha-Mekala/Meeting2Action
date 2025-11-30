# src/app.py - FastAPI app with Netflix-style UI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path

from .coordinator import Coordinator

app = FastAPI(title="Meeting2Action – Enterprise Console (Local)")

# Ensure reports dir exists
reports_dir = Path("artifacts/reports")
reports_dir.mkdir(parents=True, exist_ok=True)

# Mount static and reports
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/artifacts/reports", StaticFiles(directory=str(reports_dir)), name="reports")

templates = Jinja2Templates(directory="templates")

class ParseRequest(BaseModel):
  transcript: str
  meeting_id: str = "meeting-1"

coord = Coordinator()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
  return {"status": "ok"}

@app.post("/parse_transcript/")
def parse_transcript(req: ParseRequest):
  return coord.run_pipeline(req.transcript, req.meeting_id)