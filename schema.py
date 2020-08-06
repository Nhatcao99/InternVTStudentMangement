from typing import List, Optional
from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str

class Student(StudentBase):
    id : int
    name : str
    class_id: Optional[int]
    class Config:
        orm_mode = True

class StudentCreate(StudentBase):
    pass

class ClassBase(BaseModel):
    name: str

class ClassAdd(BaseModel):
    id: int
    class Config:
        orm_mode = True

class Class(ClassBase):
    id : int
    students: List[Student] = []
    class Config:
        orm_mode = True