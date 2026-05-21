from datetime import datetime

class Note:
    def __init__ (self, employee_name, content, case_reference=None, created_at=None):
        self.employee_name = employee_name
        self.content = content
        self.case_reference = case_reference or "General"
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict (self):
        return {
            "employee_name": self.employee_name, 
            "content": self.content,
            "case_reference": self.case_reference,
            "created_at": self.created_at
        }
        
    def __str__(self):
        return f"[{self.created_at}] {self.employee_name}: {self.content}"
    




