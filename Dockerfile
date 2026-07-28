FROM python:3.11-alpine

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]