from pydantic import BaseModel

class Sign_up_model(BaseModel):
    fullname: str
    username: str
    password: str
    role: str

class Sign_in_model(BaseModel):
    username:str
    password:str