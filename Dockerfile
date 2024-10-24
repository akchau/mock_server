FROM python:3.10-slim
WORKDIR /app
COPY req.txt /app
RUN pip install -r req.txt && \
    pip uninstall watchfiles -y
ADD  . /app
ARG APP_PORT
EXPOSE $APP_PORT
CMD ["python", "main.py", "runserver"]