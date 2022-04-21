FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /homework_03

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD uvicorn app:app --host=0.0.0.0 --port=8000