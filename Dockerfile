FROM python:3.8 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /code

CMD [ "python", "./app.py" ]
