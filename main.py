import uvicorn
from settings import settings


def runserver(*args, **kwargs):
    kwargs['reload'] = True
    uvicorn.run(
        'app:app',
        host="0.0.0.0",
        port=settings.APP_PORT,
        **kwargs
    )


if __name__ == "__main__":
    runserver()
