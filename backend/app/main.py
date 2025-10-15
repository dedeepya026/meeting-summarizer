from fastapi import FastAPI
from app.api import transcribe, summarize
from app.config import settings


app = FastAPI()
app.include_router(transcribe.router, prefix='/v1/transcribe')
app.include_router(summarize.router, prefix='/v1/summaries')


@app.get('/')
def root():
    return {"status": "meeting summarizer backend"}


# Run with: uvicorn app.main:app --reload --port 8000