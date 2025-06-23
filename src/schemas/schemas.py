from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List


class Video(BaseModel):
    name: str | None = None
    description: str | None = None


class CommentBase(BaseModel):
    content: str = Field(..., max_length=100)


class CommentCreate(CommentBase):
    video_id: UUID
    user_id: UUID


class CommentResponse(CommentBase):
    id: UUID
    video_id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class VideoWithComments(BaseModel):
    id: UUID
    filename: str
    url: str
    caption: str | None = None
    created_at: datetime
    likes_count: int
    comments_count: int
    comments: List[CommentResponse] = []

    class Config:
        from_attributes = True
