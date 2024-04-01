from tinydb import TinyDB,Query
import sys
import os
# Remove these two lines after finishing the development of thid module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import random
from students_api.student import Student


db = TinyDB('db/db.json')

Students = Query()

classNames = ['English', 'Hebrew', 'Computers', 'Dance', 'Engineering', 'Arbic', 'chemistry', 'Sports']
names =['John', 'Sam', 'Tamy', 'Sandy', 'Tom', 'Marwan', 'Sally']

#add initial values to the db
def seed():
    if(len(db.all()) != 0):
        print("db was seeded!")
        return
    names_add = random.sample(names,7)
    for i in range(0,7):
        db.insert(document={'name': names_add[i] ,'age': random.randint(18,60), 'classes': random.sample(classNames,random.randint(2,4))})


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