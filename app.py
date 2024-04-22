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


@router.api_route("/", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def root(request: Request):
    headers = dict(request.headers)
    if request.method == "GET":
        return JSONResponse({"message": f"GET_method_request_handled, params={dict(request.query_params)}, headers={headers}"}, status_code=200)
    elif request.method == "POST":
        payload = await request.json()
        return JSONResponse({"message": f"POST_method_request_handled, data={payload}, headers={headers}"}, status_code=200)
    elif request.method == "DELETE":
        return JSONResponse({"message": f"DELETE_method_request_handled, params={dict(request.query_params)}, headers={headers}"}, status_code=200)
    elif request.method == "PATCH":
        payload = await request.json()
        return JSONResponse({"message": f"PATCH_method_request_handled, data={payload}, headers={headers}"}, status_code=200)
    elif request.method == "PUT":
        payload = await request.json()
        return JSONResponse({"message": f"PUT_method_request_handled, data={payload}, headers={headers}"}, status_code=200)

app.include_router(router)
