# Legal Notes API

A production-grade REST API for managing legal employee notes,
built with FastAPI and PostgreSQL. Deployed on Render.

## Live API
- Base URL: https://legal-notes-api.onrender.com
- Documentation: https://legal-notes-api.onrender.com/docs

## Features
- Full CRUD operations for legal employee notes
- Search notes by employee name and case reference
- PostgreSQL database with indexed queries
- Input validation and graceful error handling
- Auto-generated interactive API documentation
- Production deployment with cloud database

## Project Structure
legal-notes-api/
├── models/
│   ├── init.py
│   ├── note.py
│   └── db_note.py
├── managers/
│   ├── init.py
│   └── note_manager.py
├── database.py
├── main.py
├── Procfile
├── runtime.txt
├── requirements.txt
└── .env.example

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API status |
| GET | /health | Health check |
| GET | /notes | Get all notes |
| POST | /notes | Create a new note |
| GET | /notes/{employee_name} | Get notes by employee |
| GET | /notes/case/{case_reference} | Get notes by case |
| GET | /notes/count/total | Get total note count |
| DELETE | /notes/{employee_name} | Delete employee notes |

## Request Body (POST /notes)
```json
{
    "employee_name": "Ali Hassan",
    "content": "Reviewed NDA for merger deal",
    "case_reference": "CASE-001"
}
```

## Local Setup
```bash
git clone https://github.com/AMRQ10/legal-notes-api
cd legal-notes-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Add DATABASE_URL to .env
uvicorn main:app --reload
```

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Render (deployment)

## Progress Log
- **Day 6 — May 8:** FastAPI endpoints with case reference support
- **Day 8 — May 22:** PostgreSQL database integration via SQLAlchemy
- **Day 9 — May 24:** Production deployment on Render with cloud database

## Author
Abdul Monim Rehan 
[GitHub](https://github.com/AMRQ10)