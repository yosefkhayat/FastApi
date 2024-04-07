from fastapi import APIRouter, Depends
from db import student_db_fns
from classes.student import Student
from auth.auth_bearer import JWTBearer
from loggings.logging_fns import log

#router to students
router = APIRouter(
    prefix = '/students',
    tags = ['Students router']
)

#Get all Students
@router.get('/',dependencies=[Depends(JWTBearer(role='all'))])
def getAllStudents():
    students = student_db_fns.getAllStudents()
    if len(students) == 0:
        return {
            "message" : "Database is empty!"
        }
    else:
        return students


#get student by name
@router.get('/get-by-name',dependencies=[Depends(JWTBearer(role='all'))])
def getStudentByName(name:str):
    student = student_db_fns.getStudentByName(name)
    if len(student) == 0:
        return {
            "message" : f'no student by name {name}'
        }
    else:
        return student

#get student by id
@router.get('/get-by-id',dependencies=[Depends(JWTBearer(role='all'))])
def getStudentById(id:int):
    student = student_db_fns.getStudentById(id)
    if student == None:
        return {
            "message" : f'no student by id : {id}'
        }
    else:
        return student

#get students names in class
@router.get('/get-by-class',dependencies=[Depends(JWTBearer(role=['admin']))])
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
@router.post('/add',dependencies=[Depends(JWTBearer(role=['admin']))])
@log
def create_student(student: Student):
    student_db_fns.addStudent(student)
    return{
            "message" : "student was created successfully"
        }


#delete student by id
@router.delete('/del-by-id',dependencies=[Depends(JWTBearer(role='all'))])
@log
def deleteById(id:int):
    if student_db_fns.getStudentById(id)== None:
        return {
            "message" : f'no student by id : {id}'
        }
    student_db_fns.deleteStudentByID(id)
    return {
            "message" : f'deleted student with id : {id}'
        }


#delete all student 
@router.delete('/del-all',dependencies=[Depends(JWTBearer(role=['admin']))])
@log
def delete_all_students():
    student_db_fns.deleteAllStudent()
    return {
            "message" : f'deleted all student'
        }
