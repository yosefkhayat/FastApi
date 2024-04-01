from fastapi import APIRouter
from db import db
from .student import Student

#router to students
router = APIRouter(
    prefix = '/students',
    tags = ['Students router']
)

#Get all Students
@router.get('/')
def getAllStudents():
    students = db.getAllStudents()
    if len(students) == 0:
        return {
            "message" : "Database is empty!"
        }
    else:
        return students


#get student by name
@router.get('/get-by-name')
def getStudentByName(name:str):
    student = db.getStudentByName(name)
    if len(student) == 0:
        return {
            "message" : f'no student by name {name}'
        }
    else:
        return student

#get students names in class
@router.get('/get-by-class')
def getStudentsInClass(className:str):
    studentsNames = []
    students = db.getAllStudentInClass(className)
    if len(students) == 0:
        return {
            "message" : "No students"
        }
    else:
        for student in students:
            studentsNames.append(student["name"])
        return studentsNames

#add student to the database
@router.post('/add/{}')
def create_student(student: Student):
    db.addStudent(student)
    return{
            "message" : "student was created successfully"
        }

