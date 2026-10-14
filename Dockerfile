FROM python:3.15-alpine

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]