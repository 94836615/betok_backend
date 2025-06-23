from sqlalchemy.orm import Session
from sqlalchemy import func, select
from src.models.comments import Comment
from uuid import UUID
from typing import List, Optional
import uuid


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
    # Convert string to UUID objects
    video_uuid = uuid.UUID(video_id)
    user_uuid = uuid.UUID(user_id)

    new_comment = Comment(video_id=video_uuid, user_id=user_uuid, content=content)
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
    # Convert string to UUID object
    video_uuid = uuid.UUID(video_id)

    return db.execute(
        select(Comment)
        .where(Comment.video_id == video_uuid)
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
    # Convert string to UUID objects
    comment_uuid = uuid.UUID(comment_id)
    user_uuid = uuid.UUID(user_id)

    comment = db.execute(
        select(Comment).where(Comment.id == comment_uuid, Comment.user_id == user_uuid)
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
    # Convert string to UUID object
    video_uuid = uuid.UUID(video_id)

    count = db.execute(
        select(func.count(Comment.id)).where(Comment.video_id == video_uuid)
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
    # Convert string to UUID object
    comment_uuid = uuid.UUID(comment_id)

    return db.execute(
        select(Comment).where(Comment.id == comment_uuid)
    ).scalar_one_or_none()
