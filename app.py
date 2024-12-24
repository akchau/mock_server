from io import StringIO
import logging
import time
from json import JSONDecodeError

from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, StreamingResponse
from settings import settings


logger = logging.getLogger(__name__)

origins = ["*"]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


router = APIRouter()


async def decode_payload(request: Request) -> dict | None | str:
    try:
        payload = await request.json()
    except JSONDecodeError:
        payload = None
    return payload


@router.api_route("/{path:path}",
                  methods=["GET", "POST", "PUT",
                           "DELETE", "PATCH", "OPTIONS"])
async def root(request: Request, path: str):
    headers = dict(request.headers)
    payload = await decode_payload(request)
    with_credentials = payload.get(
        "withCredentials") if isinstance(payload, dict) else None
    read_delay = settings.READ_DELAY
    if read_delay > 0:
        time.sleep(read_delay)
    message = (f"{request.method}-запрос, путь=/{path}, "
               f"params={dict(request.query_params)}, "
               f"headers={headers}, data={payload}, "
               f"withCredentials={with_credentials}")
    if settings.FILE:
        file_stream = StringIO(message*100)
        headers = {
            "Content-Disposition": "attachment; filename=report.txt"
        }
        return StreamingResponse(file_stream, media_type="text/plain", headers=headers)
    logger.debug(message)
    if str(settings.RESPONSE_CODE).startswith('2'):
        return JSONResponse({"message": message}, status_code=settings.RESPONSE_CODE)
    raise HTTPException(status_code=settings.RESPONSE_CODE, detail="Это детали ошибки.")


app.include_router(router)
