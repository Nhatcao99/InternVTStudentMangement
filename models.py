from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
import database
class Student(database.Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String)
    class_id = Column(Integer, ForeignKey("class.id"))
    class_r = relationship("Class",back_populates = "student")

class Class(database.Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key =True, index = True)
    name = Column(String, index = True) # Index = unique
    student = relationship("Student",back_populates = "class_r")
    
