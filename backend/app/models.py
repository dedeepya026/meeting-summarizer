from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Transcript(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    transcript_text: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Summary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transcript_id: int
    summary_text: Optional[str] = None
    decisions: Optional[str] = None # JSON string
    action_items: Optional[str] = None # JSON string
    created_at: datetime = Field(default_factory=datetime.utcnow)