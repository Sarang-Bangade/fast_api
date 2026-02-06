from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return{'message': 'Hello Sarang I am from FASTAPI'}

@app.get("/sarang")
def sarang():
    return{'message' : 'MY name is sarang'}