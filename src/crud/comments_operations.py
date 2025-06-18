from sqlalchemy.orm import Session
from sqlalchemy import func, select
from src.models.comments import Comment
from uuid import UUID
from typing import List, Optional


def create_comment(db: Session, video_id: str, user_id: str, content: str) -> Comment:
    """
    Create a new comment for a video.
    
    Args:
        db: Database session
        video_id: ID of the video to comment on
        user_id: ID of the user making the comment
        content: Content of the comment (max 100 characters)
        
    Returns:
        The created comment
    """
    new_comment = Comment(video_id=video_id, user_id=user_id, content=content)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_video_comments(db: Session, video_id: str, skip: int = 0, limit: int = 100) -> List[Comment]:
    """
    Get comments for a specific video.
    
    Args:
        db: Database session
        video_id: ID of the video to get comments for
        skip: Number of comments to skip (for pagination)
        limit: Maximum number of comments to return
        
    Returns:
        List of comments for the video
    """
    return db.execute(
        select(Comment)
        .where(Comment.video_id == video_id)
        .order_by(Comment.created_at.desc())
        .offset(skip)
        .limit(limit)
    ).scalars().all()


def delete_comment(db: Session, comment_id: str, user_id: str) -> bool:
    """
    Delete a comment.
    
    Args:
        db: Database session
        comment_id: ID of the comment to delete
        user_id: ID of the user trying to delete the comment
        
    Returns:
        True if the comment was deleted, False otherwise
    """
    comment = db.execute(
        select(Comment).where(Comment.id == comment_id, Comment.user_id == user_id)
    ).scalar_one_or_none()
    
    if comment:
        db.delete(comment)
        db.commit()
        return True
    return False


def count_video_comments(db: Session, video_id: str) -> int:
    """
    Count the number of comments for a video.
    
    Args:
        db: Database session
        video_id: ID of the video to count comments for
        
    Returns:
        Number of comments for the video
    """
    count = db.execute(
        select(func.count(Comment.id)).where(Comment.video_id == video_id)
    ).scalar_one()
    
    return count


def get_comment_by_id(db: Session, comment_id: str) -> Optional[Comment]:
    """
    Get a comment by its ID.
    
    Args:
        db: Database session
        comment_id: ID of the comment to get
        
    Returns:
        The comment if found, None otherwise
    """
    return db.execute(
        select(Comment).where(Comment.id == comment_id)
    ).scalar_one_or_none()