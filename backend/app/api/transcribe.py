from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from sqlmodel import Session, create_engine
from app.models import Transcript, SQLModel
from app.config import settings
from app.services.asr import transcribe_file


router = APIRouter()


engine = create_engine(settings.DATABASE_URL, echo=False)
SQLModel.metadata.create_all(engine)


@router.post('/', status_code=201)
async def upload_audio(file: UploadFile = File(...)):
    # save to tmp
    if not file.filename:
        raise HTTPException(400, 'no filename')
    tmp_dir = './uploads'
    os.makedirs(tmp_dir, exist_ok=True)
    path = os.path.join(tmp_dir, file.filename)
    with open(path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)


    # insert record
    with Session(engine) as session:
        t = Transcript(filename=file.filename)
        session.add(t)
        session.commit()
        session.refresh(t)
        transcript_id = t.id


    # transcribe synchronously (for demo). For production use background tasks/queue.
    text = transcribe_file(path)


    with Session(engine) as session:
        t = session.get(Transcript, transcript_id)
        t.transcript_text = text
        session.add(t)
        session.commit()


    return {"transcript_id": transcript_id, "status": "done"}


@router.get('/{id}')
def get_transcript(id: int):
    with Session(engine) as session:
        t = session.get(Transcript, id)
        if not t:
            raise HTTPException(404, 'not found')
        return {"id": t.id, "filename": t.filename, "transcript_text": t.transcript_text}