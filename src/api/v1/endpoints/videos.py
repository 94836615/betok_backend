from main import app


@app.get("/videos")
async def videos():
    return {"data": "Videos list"}

@app.post("/videos")
async def create_video():
    return {"data": "Video created successfully"}