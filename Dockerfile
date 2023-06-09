FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]
EXPOSE 5000/tcp
