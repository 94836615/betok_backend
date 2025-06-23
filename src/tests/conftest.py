import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.core.db import Base, get_db
from main import app

# Explicitly load pytest-asyncio plugin
pytest_plugins = ["pytest_asyncio"]

# Create an in-memory SQLite database for testing
@pytest.fixture(scope="function")
def test_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create the tables
    Base.metadata.create_all(bind=engine)

    # Create a session
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Override the get_db dependency
@pytest.fixture(scope="function")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

# Mock MinIO client
@pytest.fixture(scope="function")
def mock_minio():
    with patch("src.core.config.settings.minio_client") as mock:
        # Configure the mock
        mock.stat_object.return_value = MagicMock(
            size=1024,
            content_type="video/mp4"
        )
        yield mock

# Mock video upload function
@pytest.fixture(scope="function")
def mock_video_upload():
    with patch("src.crud.video_upload.video_upload") as mock:
        mock.return_value = {
            "filename": "test_video_123.mp4"
        }
        yield mock
