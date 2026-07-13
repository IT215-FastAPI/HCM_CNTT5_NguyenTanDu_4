from pydantic import BaseModel, Field
from database import get_db

class ClassSection(BaseModel):
    subject_name: str
    class_code: str
    teacher_name: str
    student_count: str

