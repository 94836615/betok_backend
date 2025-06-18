import uuid
from fastapi import UploadFile, File
from minio import S3Error

from src.core.config import settings


async def video_upload(file: UploadFile = File(...)):
    contents = await file.read()
    file_size = len(contents)
    if file_size == 0:
        raise ValueError("Empty file")

    file.file.seek(0)

    if '.' in file.filename:
        ext = file.filename.split('.')[-1].lower()
    else:
        ext = "mp4"

    object_name = f"{uuid.uuid4().hex}.{ext}"

    bucket_name = "videos"
    if not settings.minio_client.bucket_exists(bucket_name):
        settings.minio_client.make_bucket(bucket_name)

    try:
        settings.minio_client.put_object(
            bucket_name,  # bucket name
            object_name,  # object name
            file.file,  # data as stream
            file_size,  # length
            content_type=file.content_type or "video/mp4"  # keyword argument
        )
    except S3Error as e:
        raise S3Error(f"Error uploading video: {e}")

    return {"message": "Upload success", "size": file_size, "filename": object_name}
