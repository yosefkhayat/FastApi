from fastapi import FastAPI

app = FastAPI()

#test the server is up
@app.get("/test")
def test():
    return "The server is working properly!"