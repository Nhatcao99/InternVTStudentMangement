from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schema
import database
from typing import List

models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

#Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def welcome():
    return {"Message" : "Success"}

@app.post("/createClass/", response_model = schema.ClassAdd)
def create_Class(classes: schema.ClassAdd, db: Session = Depends(get_db)):
    return crud.create_class(db = db, classes = classes)

@app.get("/getClassStudent/{class_id}", response_model = schema.Class)
def get_class_student(class_id: int, db: Session = Depends(get_db)):
    return crud.get_class_student(db = db, class_id = class_id)

@app.get("/getAllClass/", response_model = List[schema.ClassAdd])
def get_all_class(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_all_class(db = db, skip = 0, limit = 100)

@app.post("/updateClass/{class_id}", response_model = schema.ClassBase) 
def update_class(classes: schema.ClassBase, db: Session = Depends(get_db)):
    return crud.update_class(db = db, clasese = classes) 

@app.get("/deleteClass/{class_id}")
def delete_class(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_class(db = db, class_id = class_id)

@app.post("/createStudent/", response_model = schema.Student)
def create_student(student: schema.Student, db: Session = Depends(get_db)):
    return crud.create_student(db = db, student = student)

@app.get("/getStudent/{student_id}", response_model = schema.Student)
def get_one_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_one_student(student_id = student_id, db = db)

@app.get("/getAllStudent/", response_model = List[schema.Student])
def get_all_student(db: Session = Depends(get_db)):
    return crud.get_all_student(db = db, skip = 0, limit=100)

@app.post("/updateStudent/{student_id}", response_model = schema.StudentBase)
def update_student(student: schema.StudentBase, db: Session = Depends(get_db)):
    return update_student(db = db, student = schema.Student)

@app.post("/deleteStudent/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db = db, student_id = student_id)