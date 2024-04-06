from tinydb import TinyDB,Query
import sys
import os
# Remove these two lines after finishing the development of thid module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import random
from classes.student import Student
from db.auth_db_fns import load_data_from_json as l


db = TinyDB('db/students_data.json')

Students = Query()

#add initial values to the db
def seed():
    if(len(db.all()) != 0):
        print("db was seeded!")
        return
    data = l("db/hardcoded_data.json")
    names_add = random.sample(data['names'],7)
    for i in range(0,7):
        db.insert(document={'name': names_add[i] ,'age': random.randint(18,60), 'classes': random.sample(data['classNames'],random.randint(2,4))})


def getAllStudents():
    return db.all()

def getStudentByName(name):
    return db.search(Students.name == name)

def getStudentById(id :int):
    return db.get(doc_id=id)

def addStudent(student: Student):
    db.insert(document={ 'name':student.name, 'age': student.age, 'classes': student.classes})
    print("the student added succecful")

def getAllStudentInClass(className):
    return db.search(Students.classes.any(className))



#seed()


#x = student.Student(name="tesla",age=35,classes=[classNames[4]])
#db.insert(document={'name': x.name,'age': x.age, 'classes': x.classes})
#for i in x:
#   print(i)