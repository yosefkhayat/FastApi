from fastapi import APIRouter, Depends
from db import student_db_fns
from classes.student import Student
from auth.auth_bearer import JWTBearer


#router to students
router = APIRouter(
    prefix = '/students',
    tags = ['Students router']
)

#Get all Students
@router.get('/',dependencies=[Depends(JWTBearer(role='guest'))])
def getAllStudents():
    students = student_db_fns.getAllStudents()
    if len(students) == 0:
        return {
            "message" : "Database is empty!"
        }
    else:
        return students


#get student by name
@router.get('/get-by-name',dependencies=[Depends(JWTBearer(role='guest'))])
def getStudentByName(name:str):
    student = student_db_fns.getStudentByName(name)
    if len(student) == 0:
        return {
            "message" : f'no student by name {name}'
        }
    else:
        return student

#get students names in class
@router.get('/get-by-class',dependencies=[Depends(JWTBearer(role='admin'))])
def getStudentsInClass(className:str):
    studentsNames = []
    students = student_db_fns.getAllStudentInClass(className)
    if len(students) == 0:
        return {
            "message" : "No students"
        }
    else:
        for student in students:
            studentsNames.append(student["name"])
        return studentsNames

#add student to the database
@router.post('/add',dependencies=[Depends(JWTBearer(role='admin'))])
def create_student(student: Student):
    student_db_fns.addStudent(student)
    return{
            "message" : "student was created successfully"
        }

