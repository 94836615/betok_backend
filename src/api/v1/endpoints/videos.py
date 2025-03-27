from fastapi import APIRouter, UploadFile, File

import logging

from src.crud.video_upload import video_upload

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/videos", status_code=200)
def get_videos():
    return "Videos"


@router.post("/videos", status_code=201)
async def post_video(video: UploadFile = File(...)):
    logger.info("Video received:", video.filename)
    contents = await video.read()
    logger.info("File size:", len(contents))
    if len(contents) == 0:
        return {"error": "Bestand is leeg"}

    # Reset file pointer
    video.file.seek(0)

    return await video_upload(video)
