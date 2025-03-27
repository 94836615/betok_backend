from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.endpoints import videos

from src.core.config import settings

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://betok.noahnap.nl"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(videos.router, prefix=settings.prefix)


@app.get("/")
async def root():
    return {"message": "Server is running"}
