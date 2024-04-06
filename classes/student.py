from pydantic import BaseModel

class Student(BaseModel):
    name : str
    age : int
    classes : list[str]