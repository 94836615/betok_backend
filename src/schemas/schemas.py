from pydantic import BaseModel


class Video(BaseModel):
    name: str | None = None
    description: str | None = None
