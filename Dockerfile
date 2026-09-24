FROM python:3.14-alpine

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]