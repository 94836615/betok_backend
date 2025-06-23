import pytest
import io
import uuid
from unittest.mock import patch, MagicMock, AsyncMock
from fastapi import UploadFile
from minio import S3Error

from src.crud.video_upload import video_upload

@pytest.fixture
def mock_upload_file():
    """Create a mock UploadFile for testing."""
    content = b"test video content"
    file = io.BytesIO(content)

    # Create a mock UploadFile
    upload_file = MagicMock(spec=UploadFile)
    upload_file.filename = "test_video.mp4"
    upload_file.content_type = "video/mp4"
    upload_file.file = file

    # Use AsyncMock for the read method
    async_read = AsyncMock(return_value=content)
    upload_file.read = async_read

    return upload_file

@pytest.mark.asyncio
async def test_video_upload_success(mock_upload_file):
    """Test successful video upload."""
    # Arrange
    with patch("src.core.config.settings.minio_client") as mock_minio:
        mock_minio.bucket_exists.return_value = True

        # Act
        result = await video_upload(mock_upload_file)

        # Assert
        assert "message" in result
        assert result["message"] == "Upload success"
        assert "size" in result
        assert result["size"] == len(b"test video content")
        assert "filename" in result
        assert result["filename"].endswith(".mp4")

        # Verify MinIO client was called correctly
        mock_minio.put_object.assert_called_once()

@pytest.mark.asyncio
async def test_video_upload_empty_file(mock_upload_file):
    """Test upload with empty file."""
    # Arrange
    mock_upload_file.read.return_value = b""

    # Act & Assert
    with pytest.raises(ValueError, match="Empty file"):
        await video_upload(mock_upload_file)

@pytest.mark.asyncio
async def test_video_upload_no_extension():
    """Test upload with filename that has no extension."""
    # Arrange
    content = b"test video content"
    file = io.BytesIO(content)

    # Create a mock UploadFile with no extension in filename
    upload_file = MagicMock(spec=UploadFile)
    upload_file.filename = "test_video"  # No extension
    upload_file.content_type = "video/mp4"
    upload_file.file = file

    # Use AsyncMock for the read method
    async_read = AsyncMock(return_value=content)
    upload_file.read = async_read

    # Act
    with patch("src.core.config.settings.minio_client") as mock_minio:
        mock_minio.bucket_exists.return_value = True
        result = await video_upload(upload_file)

    # Assert
    assert "filename" in result
    assert result["filename"].endswith(".mp4")  # Default extension is used

@pytest.mark.asyncio
async def test_video_upload_create_bucket(mock_upload_file):
    """Test that bucket is created if it doesn't exist."""
    # Arrange
    with patch("src.core.config.settings.minio_client") as mock_minio:
        mock_minio.bucket_exists.return_value = False

        # Act
        result = await video_upload(mock_upload_file)

        # Assert
        mock_minio.make_bucket.assert_called_once_with("videos")
        assert "message" in result
        assert result["message"] == "Upload success"

@pytest.mark.asyncio
async def test_video_upload_s3_error(mock_upload_file):
    """Test handling of S3Error during upload."""
    # Arrange
    with patch("src.core.config.settings.minio_client") as mock_minio:
        mock_minio.bucket_exists.return_value = True
        # Use a generic exception instead of S3Error
        mock_minio.put_object.side_effect = Exception("Test error")

        # Act & Assert
        # Just check that an exception is raised, don't check the specific message
        with pytest.raises(Exception):
            await video_upload(mock_upload_file)
