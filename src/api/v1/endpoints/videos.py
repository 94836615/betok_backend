import uuid
from datetime import UTC, datetime

from fastapi import APIRouter, UploadFile, File

import logging

from sqlalchemy.orm import Session

from src.core.db import engine
from src.crud.video_upload import video_upload
from src.models.video import Video

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/videos", status_code=200)
def get_videos():
    return "Videos"


@router.post("/videos", status_code=201)
async def post_video(video: UploadFile = File(...)):
    logger.info("Video received: %s", video.filename)
    contents = await video.read()
    logger.info("File size: %d", len(contents))
    if len(contents) == 0:
        return {"error": "Bestand is leeg"}

    # Reset file pointer
    video.file.seek(0)

    # Upload to Minio
    result = await video_upload(video)
    object_name = result["filename"]

    url = f"https://console.noahnap.nl/videos/{object_name}"

    # Adds metadata to the response
    with Session(engine) as db:
        video_entry = Video(
            id=uuid.uuid4(),
            filename=video.filename,
            url=url,
            created_at=datetime.now(UTC),
            caption=None,  # later via Form(...)
            user_id=None  # later via auth
        )
        db.add(video_entry)
        db.commit()
        db.refresh(video_entry)

    return {
        "message": "Upload success",
        "video_id": str(video_entry.id),
        "url": url
    }
