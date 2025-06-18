from fastapi import APIRouter
import logging

from starlette.responses import JSONResponse

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/followers", status_code=200)
async def get_followers():
    followers = [
        {
            "id": "betok_device_id_v1",
            "name": "betok_device_id_v1",
            "amount_followers": 0,
        }
    ]
    logger.info("Fetched followers successfully")
    return JSONResponse(status_code=200, content={"followers": followers})
