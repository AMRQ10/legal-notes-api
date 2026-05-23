from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models.db_note import NoteDB
from dotenv import load_dotenv
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Legal Notes API",
    description="A production-grade API for managing legal employee notes",
    version="2.0.0"
)

APP_NAME = os.getenv("APP_NAME", "Legal Notes API")

class NoteRequest(BaseModel):
    employee_name: str
    content: str
    case_reference: str = "General"

@app.get("/")
def root():
    return {"message": f"{APP_NAME} is running", "version": "2.0.0"}

@app.get("/notes")
def get_all_notes(db: Session = Depends(get_db)):
    notes = db.query(NoteDB).all()
    return {
        "count": len(notes),
        "notes": [note.to_dict() for note in notes]
    }

@app.post("/notes", status_code=201)
def add_note(note_request: NoteRequest, db: Session = Depends(get_db)):
    if not note_request.employee_name.strip():
        raise HTTPException(status_code=400, detail="Employee name cannot be empty")
    if not note_request.content.strip():
        raise HTTPException(status_code=400, detail="Note content cannot be empty")

    new_note = NoteDB(
        employee_name=note_request.employee_name.strip(),
        content=note_request.content.strip(),
        case_reference=note_request.case_reference.strip()
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {
        "message": f"Note added for {new_note.employee_name}",
        "note" : new_note.to_dict()
    }

@app.get("/notes/{employee_name}")
def get_notes_by_employee(employee_name: str, db: Session = Depends(get_db)):
    notes = db.query(NoteDB).filter(
        NoteDB.employee_name.ilike(f"%{employee_name}%")
    ).all()

    if not notes:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for {employee_name}"
        )

    return {
        "employee": employee_name,
        "count": len(notes),
        "notes": [note.to_dict() for note in notes]
    }

@app.get("/notes/count/total")
def get_note_count(db: Session = Depends(get_db)):
    count = db.query(NoteDB).count()
    return {"total_notes": count}

@app.get("/notes/case/{case_reference}")
def get_notes_by_case(case_reference: str, db: Session = Depends(get_db)):
    notes = db.query(NoteDB).filter(
            NoteDB.case_reference.ilike(f"%{case_reference}")
        ).all()

    if not notes:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for case {case_reference}"
        )

    return {
        "case_reference": case_reference,
        "count": len(notes),
        "notes": [note.to_dict() for note in notes]
    }

@app.delete("/notes/{employee_name}", status_code=200)
def delete_employee_notes(employee_name: str, db: Session = Depends(get_db)):
    notes = db.query(NoteDB).filter(
        NoteDB.employee_name.ilike(f"%{employee_name}%")
    ).all()

    if not notes:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for {employee_name}"
        )
    for note in notes:
        db.delete(note)
    db.commit()
    
    return{"message": f"Deleted {len(notes)} notes for {employee_name}"}

