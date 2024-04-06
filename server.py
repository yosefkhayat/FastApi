from fastapi import FastAPI
from routes import student_api,auth_api

server = FastAPI()

server.include_router(student_api.router)
server.include_router(auth_api.router)
#test the server is up
@server.get("/test")
def test():
    return "The server is working properly!"