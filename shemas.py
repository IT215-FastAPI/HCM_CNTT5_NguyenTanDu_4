from pydantic import BaseModel
from database import get_db

class ClassSection(BaseModel):
    subject_name: str 
    class_code: str
    teacher_name: str
    student_count: int



class ClassSectionResponce(BaseModel):
    id: int
    subject_name: str
    class_code: str
    teacher_name: str
    student_count: int
    
    model_config = {"from_attributes": True}