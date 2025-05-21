from sqlalchemy.orm import Session
from sqlalchemy import func, select
from src.models.likes import Like


def like_video(db: Session, video_id: str, user_id: str):
    # Check if like already exists
    existing_like = db.execute(
        select(Like).where(Like.video_id == video_id, Like.user_id == user_id)
    ).scalar_one_or_none()
    
    if existing_like:
        return existing_like
    
    # Create new like
    new_like = Like(video_id=video_id, user_id=user_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like


def unlike_video(db: Session, video_id: str, user_id: str):
    deleted = db.execute(
        select(Like).where(Like.video_id == video_id, Like.user_id == user_id)
    ).scalar_one_or_none()
    
    if deleted:
        db.delete(deleted)
        db.commit()
        return True
    return False


def get_video_like_status(db: Session, video_id: str, user_id: str):
    existing_like = db.execute(
        select(Like).where(Like.video_id == video_id, Like.user_id == user_id)
    ).scalar_one_or_none()
    
    return bool(existing_like)


def count_video_likes(db: Session, video_id: str):
    count = db.execute(
        select(func.count(Like.id)).where(Like.video_id == video_id)
    ).scalar_one()
    
    return count