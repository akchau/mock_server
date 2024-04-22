import uvicorn


def runserver(*args, **kwargs):
    kwargs['reload'] = True
    uvicorn.run(
        'app:app',
        host="0.0.0.0",
        port=8000,
        **kwargs
    )


if __name__ == "__main__":
    runserver()
