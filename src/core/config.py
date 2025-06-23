import os
import sys
from urllib.parse import urlparse
from unittest.mock import MagicMock

from dotenv import load_dotenv
from minio import Minio
load_dotenv()


class Settings:
    prefix = os.getenv("PREFIX", "/api/v1")

    # Handle MinIO configuration
    minio_api_link = os.getenv("MINIO_API_LINK", "")

    # Create a mock MinIO client if running tests and no MinIO config is provided
    if 'pytest' in sys.modules and (not minio_api_link or minio_api_link == "https://minio.example.com"):
        minio_client = MagicMock()
        minio_client.bucket_exists.return_value = True
        minio_client.stat_object.return_value = MagicMock(
            size=1024,
            content_type="video/mp4"
        )
    else:
        # Real MinIO client for production/development
        parsed_url = urlparse(minio_api_link)
        minio_endpoint = parsed_url.netloc
        minio_client = Minio(
            minio_endpoint,
            access_key=os.environ.get("MINIO_ACCESS_KEY", ""),
            secret_key=os.environ.get("MINIO_SECRET_KEY", ""),
            secure=(parsed_url.scheme == "https")
        )

settings = Settings()
