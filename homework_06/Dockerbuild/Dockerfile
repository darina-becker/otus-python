FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST='0.0.0.0'
ENV CONFIG_NAME='ProductionConfig'

EXPOSE 5080
