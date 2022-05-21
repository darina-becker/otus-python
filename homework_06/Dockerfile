FROM python:3.9-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /hw06

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV CONFIG_NAME=DevelopmentConfig

ENV FLASK_RUN_HOST='0.0.0.0'

EXPOSE 5433
CMD flask run