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


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def root(request: Request, path: str):
    headers = dict(request.headers)
    try:
        payload = await request.json()
    except JSONDecodeError:
        payload = None

    with_credentials = payload.get("withCredentials") if payload else None

    if request.method == "GET":
        return JSONResponse({"message": f"GET-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)
    elif request.method == "POST":
        return JSONResponse({"message": f"POST-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)
    elif request.method == "DELETE":
        return JSONResponse({"message": f"DELETE-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)
    elif request.method == "PATCH":
        return JSONResponse({"message": f"PATCH-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)
    elif request.method == "PUT":
        return JSONResponse({"message": f"PUT-запрос, путь=/{path}, params={dict(request.query_params)}, headers={headers}, data={payload}, withCredentials={with_credentials}"}, status_code=200)

app.include_router(router)
