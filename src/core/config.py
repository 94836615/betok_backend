import os

from dotenv import load_dotenv
from minio import Minio

load_dotenv()


class Settings:
    prefix = os.getenv("PREFIX")
    minio_client = Minio(os.environ.get("MINIO_API_LINK"),
                         access_key=os.environ.get("MINIO_ACCESS_KEY"),
                         secret_key=os.environ.get("MINIO_SECRET_KEY"),
                         secure=True)


settings = Settings()
