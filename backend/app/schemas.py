from pydantic import BaseModel
from typing import Optional


class UploadResponse(BaseModel):
    transcript_id: int
    status: str


class TranscribeStatus(BaseModel):
    id: int
    filename: str
    transcript_text: Optional[str]


class SummarizeRequest(BaseModel):
    transcript_id: int
    tone: Optional[str] = 'concise'
    include_action_items: Optional[bool] = True


class SummaryResponse(BaseModel):
    id: int
    transcript_id: int
    summary_text: Optional[str]
    decisions: Optional[dict]
    action_items: Optional[list]