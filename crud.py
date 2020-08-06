from sqlalchemy.orm import Session
import models, schema

#Class
def create_class(db: Session, student: schema.ClassAdd):
    db_class = models.Class(id = models.id, name = models.name)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    

def get_class_student(db: Session, class_id: int): #schema will be Class
    return db.query(models.Class).filter(models.Class.id == class_id).first()

def get_all_class(db:Session, skip: int =0, limit: int = 100): #respond model will be AllClass schema
    return db.query(models.Class).offset(skip).limit(limit).all()

def update_class(db:Session, class_id: int, classes: schema.ClassBase): # change class name
    ###delete step
    name_add = classes.name
    delete_student(db = db, class_id = class_id)
    ###adding step
    db_class = models.Class(id = class_id, name = name_add)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)

def delete_class(db:Session, class_id: int): #exterminate foreign key with student
    deleted = db.query(models.Class).filter(models.Class.id == class_id).first()
    db.delete(deleted)
    db.commit()

#Student
def create_student(db: Session, student: schema.Student):
    db_student = models.Student(id = student.id, name = student.name, class_id = student.class_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

def get_one_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_all_student(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def update_student(db:Session, student_id: int, student: schema.StudentBase):
    ###delete step
    name_add = student.name
    class_id_add =  student.class_id
    delete_student(db = db, student_id = student_id)
    ###adding step
    db_student = models.Student(id=student_id, name=name_add, class_id=class_id_add)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

def delete_student(db:Session, student_id: int):
    deleted = db.query(models.Student).filter(models.Student.id == student_id).first()
    db.delete(deleted)
    db.commit()

#### def add_student()
def create_class_student(db: Session, item: schema.StudentCreate, class_id: int):
    db_student = models.Student(**student.dict(), class_id=class_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student