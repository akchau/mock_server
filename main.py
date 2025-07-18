import uvicorn
from logger import init_logger
from settings import settings

init_logger()

def runserver(*args, **kwargs):
    """ Запуск веб-сервера """
    kwargs['reload'] = True
    uvicorn.run(
        'app:app',
        host="0.0.0.0",
        port=settings.APP_PORT,
        **kwargs
    )


if __name__ == "__main__":
    runserver()
