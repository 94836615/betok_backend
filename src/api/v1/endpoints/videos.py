import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, UploadFile, File, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
import logging

from minio import S3Error
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.config import settings
from src.core.db import get_db
from src.crud.likes_operations import count_video_likes
from src.crud.comments_operations import count_video_comments
from src.crud.video_upload import video_upload
from src.models.video import Video

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/videos", status_code=200)
def get_videos(
    limit: int = Query(2, ge=2), 
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    videos = db.execute(
        select(Video).order_by(Video.created_at.desc()).limit(limit).offset(offset)
    ).scalars().all()

    result = []
    for video in videos:
        likes_count = count_video_likes(db, str(video.id))
        comments_count = count_video_comments(db, str(video.id))
        result.append({
            "id": video.id,
            "filename": video.filename,
            "url": video.url,
            "caption": video.caption,
            "created_at": video.created_at.isoformat(),
            "likes_count": likes_count,
            "comments_count": comments_count
        })

    return result

@router.post("/videos", status_code=201)
async def post_video(
    video: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    logger.info("Video received: %s", video.filename)

    try:
        upload_result = await video_upload(video)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")

    object_name = upload_result["filename"]

    try:
        stat = settings.minio_client.stat_object("videos", object_name)
    except Exception as e:
        logger.error("Error getting video metadata: %s", e)
        raise HTTPException(status_code=500, detail="Fault getting video metadata")

    video_entry = Video(
        id=uuid.uuid4(),
        filename=video.filename,
        url=f"{settings.minio_api_link}/{object_name}",
        created_at=datetime.now(timezone.utc),
        caption=None,  # later via Form(...)
        user_id=None  # later via auth
    )
    db.add(video_entry)
    db.commit()
    db.refresh(video_entry)

    return JSONResponse(
        status_code=201,
        content={
            "message": "Upload success",
            "video_id": str(video_entry.id),
            "object_name": object_name,
            "stored_filename": video.filename,
            "file_size": stat.size,
            "content_type": stat.content_type
        }
    )
