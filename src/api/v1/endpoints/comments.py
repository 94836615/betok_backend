import uuid
from fastapi import APIRouter, HTTPException, Depends, Path, Query, Body
from sqlalchemy import select
from sqlalchemy.orm import Session
import logging
from src.core.db import get_db
from src.crud.comments_operations import create_comment, get_video_comments, delete_comment, count_video_comments, get_comment_by_id
from src.models.video import Video
from src.schemas.schemas import CommentCreate, CommentResponse

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/videos/{video_id}/comments", status_code=201, response_model=CommentResponse)
def create_comment_endpoint(
        video_id: uuid.UUID = Path(...),
        user_id: uuid.UUID = Body(...),  # Temporary until auth is implemented
        content: str = Body(..., max_length=100),
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    try:
        comment = create_comment(db, str(video_id), str(user_id), content)
        return comment
    except Exception as e:
        logger.error("Error creating comment: %s", e)
        raise HTTPException(status_code=500, detail="Failed to create comment")


@router.get("/videos/{video_id}/comments", status_code=200, response_model=list[CommentResponse])
def get_comments_endpoint(
        video_id: uuid.UUID = Path(...),
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=100),
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    try:
        comments = get_video_comments(db, str(video_id), skip, limit)
        return comments
    except Exception as e:
        logger.error("Error getting comments: %s", e)
        raise HTTPException(status_code=500, detail="Failed to get comments")


@router.delete("/comments/{comment_id}", status_code=200)
def delete_comment_endpoint(
        comment_id: uuid.UUID = Path(...),
        user_id: uuid.UUID = Body(...),  # Temporary until auth is implemented
        db: Session = Depends(get_db)
):
    # Check if comment exists
    comment = get_comment_by_id(db, str(comment_id))
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    try:
        result = delete_comment(db, str(comment_id), str(user_id))
        if result:
            return {"success": True, "message": "Comment deleted successfully"}
        else:
            raise HTTPException(status_code=403, detail="You can only delete your own comments")
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error deleting comment: %s", e)
        raise HTTPException(status_code=500, detail="Failed to delete comment")


@router.get("/videos/{video_id}/comments/count", status_code=200)
def get_comments_count_endpoint(
        video_id: uuid.UUID = Path(...),
        db: Session = Depends(get_db)
):
    # Check if video exists
    video = db.execute(select(Video).where(Video.id == video_id)).scalar_one_or_none()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    try:
        count = count_video_comments(db, str(video_id))
        return {"count": count}
    except Exception as e:
        logger.error("Error counting comments: %s", e)
        raise HTTPException(status_code=500, detail="Failed to count comments")