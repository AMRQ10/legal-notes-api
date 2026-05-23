from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class NoteDB(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, nullable=False, index=True)
    content = Column(String, nullable=False)
    case_reference = Column(String, default="General", index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "content": self.content,
            "case_reference": self.case_reference,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else None

        }