from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class ClassSection(Base):
    __tablename__ = "class_sections"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_name: Mapped[str] = mapped_column(String(255))
    class_code: Mapped[str] = mapped_column(String(50))
    teacher_name: Mapped[str] = mapped_column(String(255))
    student_count: Mapped[int] = mapped_column(Integer)

