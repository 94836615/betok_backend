import uuid
from sqlalchemy import Column, UUID, ForeignKey, UniqueConstraint, DateTime
from datetime import datetime, timezone

from src.core.db import Base


class Like(Base):
    __tablename__ = "likes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    video_id = Column(UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)  # Will be a ForeignKey when user model is implemented
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Ensure a user can only like a video once
    __table_args__ = (
        UniqueConstraint('video_id', 'user_id', name='uq_video_user_like'),
    )