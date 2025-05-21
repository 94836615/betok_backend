import uuid

from sqlalchemy import Column, String, DateTime, UUID, Text
from sqlalchemy.orm import relationship
from src.core.db import Base
from datetime import datetime, UTC


class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    url = Column(Text, nullable=False)
    caption = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    user_id = Column(UUID(as_uuid=True), nullable=True)  # in toekomst ForeignKey naar users.id
    
    # Add relationship to likes
    likes = relationship("Like", cascade="all, delete-orphan", backref="video")