from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from managers.note_manager import NoteManager
from dotenv import load_dotenv
import os

from models import notes

load_dotenv()

app = FastAPI(
    title="Legal Notes API",
    description="An API for managing legal employee notes",
    version="1.0.0"
)

manager = NoteManager()

class NoteRequest(BaseModel):
    employee_name: str
    content: str
    case_reference: str = "General"

@app.get("/")
def root():
    return {"message": "Legal Notes API is running"}

@app.get("/notes")
def get_all_notes():
    notes = manager.get_all_notes()
    return{
        "count": len(notes),
        "notes": [note.to_dict() for note in notes]
    }

@app.post ("/notes", status_code=201)
def add_note(note_request: NoteRequest):
    try:
        manager.add_note(note_request.employee_name, note_request.content)
        return {"message": f"Note added for {note_request.employee_name}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/notes/{employee_name}")
def get_notes_by_employee(employee_name: str):
    results = manager.search_by_employee(employee_name)
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for {employee_name}"
        )

    return {
        "employee": employee_name,
        "count": len(results),
        "notes": [note.to_dict() for note in results]
    }

@app.get("/notes/count/total")
def get_note_count():
    return {"total_notes": manager.count()}

@app.get("/notes/case/{case_reference}")
def get_notes_by_case(case_reference: str):
    results = [
        n for n in manager.get_all_notes()
        if n.case_reference.lower() == case_reference.lower()
    ]
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for case {case_reference}"
        )
    return {
        "case_reference": case_reference
        "count": len(results)
        "notes": [note.to_dict() for note in results]
    }

@app.delete("/notes/{employee_name}", status_code=200)
def delete_employee_notes(employee_name: str):
    results = manager.search_by_employee(employee_name)
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No notes found for {employee_name}"
        )
    manager.clear_by_employee(employee_name)
    return{"message": f"All notes deleted for {employee_name}"}

