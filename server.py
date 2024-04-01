from fastapi import FastAPI
from students_api import student_api
server = FastAPI()

server.include_router(student_api.router)
#test the server is up
@server.get("/test")
def test():
    return "The server is working properly!"