from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get():
    return {"hello": "world"}

@app.get("/hello")
async def get2():
    return {"hello": "world"}
