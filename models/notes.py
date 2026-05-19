from datetime import datetime

class Note:
    def __init__ (self, employee_name, content, created_at=None):
        self.employee_name = employee_name
        self.content = content
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict (self):
        return {
            "employee_name": self.employee_name, 
            "content": self.content,
            "created_at": self.created_at
        }
        
    def __str__(self):
        return f"[{self.created_at}] {self.employee_name}: {self.content}"
    




