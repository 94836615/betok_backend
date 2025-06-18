import uuid
from sqlalchemy import Column, UUID, ForeignKey, String, DateTime, UniqueConstraint, Text
from datetime import datetime, UTC

from src.core.db import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    video_id = Column(UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)  # Will be a ForeignKey when user model is implemented
    content = Column(String(100), nullable=False)  # 100 character limit as per requirements
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))