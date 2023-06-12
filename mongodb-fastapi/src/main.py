from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def printHello():
    return "hello"

@app.get("/hello")
async def printHello2():
    return "hello3"