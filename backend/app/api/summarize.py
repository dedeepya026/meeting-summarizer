from fastapi import APIRouter, HTTPException
from sqlmodel import Session, create_engine
from app.models import Transcript, Summary, SQLModel
from app.config import settings
from app.services.summarizer import generate_summary


router = APIRouter()


engine = create_engine(settings.DATABASE_URL, echo=False)
SQLModel.metadata.create_all(engine)


@router.post('/')
def summarize(transcript_id: int):
    with Session(engine) as session:
        t = session.get(Transcript, transcript_id)
        if not t or not t.transcript_text:
            raise HTTPException(404, 'transcript missing')
        parsed = generate_summary(t.transcript_text)
        s = Summary(transcript_id=transcript_id, summary_text=parsed.get('summary'), decisions=str(parsed.get('decisions')), action_items=str(parsed.get('action_items')))
        session.add(s)
        session.commit()
        session.refresh(s)
        return {"summary_id": s.id, "summary": parsed}


@router.get('/{id}')
def get_summary(id: int):
    with Session(engine) as session:
        s = session.get(Summary, id)
        if not s:
            raise HTTPException(404, 'not found')
    return {"id": s.id, "transcript_id": s.transcript_id, "summary_text": s.summary_text, "decisions": s.decisions, "action_items": s.action_items}