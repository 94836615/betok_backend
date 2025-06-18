import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from minio import Minio
load_dotenv()


class Settings:
    prefix = os.getenv("PREFIX")

    minio_api_link = os.getenv("MINIO_API_LINK", "")
    parsed_url = urlparse(minio_api_link)
    minio_endpoint = parsed_url.netloc
    minio_client = Minio(
        minio_endpoint,
                         access_key=os.environ.get("MINIO_ACCESS_KEY"),
                         secret_key=os.environ.get("MINIO_SECRET_KEY"),
                         secure=(parsed_url.scheme == "https"))

settings = Settings()
