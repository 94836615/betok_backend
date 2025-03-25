from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/upload")
async def root():
    return {"message": "Hello Upload"}