import io
import uuid
from fastapi import UploadFile, File

from src.core.config import settings


async def video_upload(file: UploadFile = File(...)):
    contents = await file.read()
    object_name = uuid.uuid4().hex

    # Create bucket if not exists
    bucket_name = "videos"
    if not settings.minio_client.bucket_exists(bucket_name):
        settings.minio_client.make_bucket(bucket_name)

    # Upload to MinIO
    settings.minio_client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=io.BytesIO(contents),
        length=len(contents),
        content_type=file.content_type,
    )

    return {"message": "Upload success with", "size": len(contents), "filename": object_name}
