import time
from json import JSONDecodeError

from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

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


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def root(request: Request, path: str, read_delay: int = 2):
    headers = dict(request.headers)
    payload = await decode_payload(request)
    with_credentials = payload.get("withCredentials") if payload else None
    if read_delay > 0:
        time.sleep(read_delay)
    print({"message": f"{request.method}-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"})
    return JSONResponse({"message": f"{request.method}-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)


app.include_router(router)
