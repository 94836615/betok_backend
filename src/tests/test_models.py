import pytest
from datetime import datetime, UTC
import uuid
from src.models.video import Video

def test_video_model_creation():
    """Test that a Video model can be created with the expected attributes."""
    # Arrange
    video_id = uuid.uuid4()
    filename = "test_video.mp4"
    url = "http://example.com/test_video.mp4"
    caption = "Test video caption"
    created_at = datetime.now(UTC)
    user_id = uuid.uuid4()
    
    # Act
    video = Video(
        id=video_id,
        filename=filename,
        url=url,
        caption=caption,
        created_at=created_at,
        user_id=user_id
    )
    
    # Assert
    assert video.id == video_id
    assert video.filename == filename
    assert video.url == url
    assert video.caption == caption
    assert video.created_at == created_at
    assert video.user_id == user_id

def test_video_model_default_values():
    """Test that a Video model uses default values when not provided."""
    # Arrange & Act
    video = Video(
        filename="test_video.mp4",
        url="http://example.com/test_video.mp4"
    )
    
    # Assert
    assert video.id is not None  # Should have a default UUID
    assert video.created_at is not None  # Should have a default timestamp
    assert video.caption is None  # Optional field
    assert video.user_id is None  # Optional field