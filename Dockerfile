FROM python:3.10-slim

ADD  . /app

WORKDIR /app

RUN pip install -r req.txt

RUN pip uninstall watchfiles -y
#RUN pip install --upgrade pydantic

CMD ["python", "main.py", "runserver"]