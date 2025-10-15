import os
import tempfile
from openai import OpenAI
from app.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def transcribe_file(path: str) -> str:
    """Transcribe audio with OpenAI's Whisper (API). Returns transcript string."""
    # Note: this uses the newer OpenAI python client pattern. If you use the official
    # `openai` package older versions, you might need to adapt.
    with open(path, 'rb') as audio_file:
    # Whisper (classic) model name: "whisper-1"
        resp = client.audio.transcriptions.create(model='whisper-1', file=audio_file)
        text = resp.text if hasattr(resp, 'text') else resp['text']
    return text