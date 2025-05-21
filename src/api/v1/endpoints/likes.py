import uuid
from fastapi import APIRouter, HTTPException, Depends, Path, Query, Body
from sqlalchemy import select
from sqlalchemy.orm import Session
import logging
from src.core.db import get_db
from src.crud.likes_operations import get_video_like_status, unlike_video, like_video, count_video_likes
from src.models.video import Video

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/videos/{video_id}/like", status_code=200)
def like_video_endpoint(
        video_id: uuid.UUID = Path(...),
        user_id: uuid.UUID = Body(...),  # Temporary until auth is implemented
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    try:
        like = like_video(db, str(video_id), str(user_id))
        return {"success": True, "message": "Video liked successfully"}
    except Exception as e:
        logger.error("Error liking video: %s", e)
        raise HTTPException(status_code=500, detail="Failed to like video")


@router.delete("/videos/{video_id}/like", status_code=200)
def unlike_video_endpoint(
        video_id: uuid.UUID = Path(...),
        user_id: uuid.UUID = Body(...),  # Temporary until auth is implemented
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    result = unlike_video(db, str(video_id), str(user_id))
    if result:
        return {"success": True, "message": "Video unliked successfully"}
    else:
        return {"success": False, "message": "Video was not liked"}


@router.get("/videos/{video_id}/like-status", status_code=200)
def get_like_status(
        video_id: uuid.UUID = Path(...),
        user_id: uuid.UUID = Query(...),  # Temporary until auth is implemented
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    is_liked = get_video_like_status(db, str(video_id), str(user_id))
    likes_count = count_video_likes(db, str(video_id))

    return {
        "is_liked": is_liked,
        "likes_count": likes_count
    }
