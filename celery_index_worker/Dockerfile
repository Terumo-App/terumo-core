FROM python:3.10.11-slim-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /celery_index_worker
# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir -p /celery_index_worker/file_storage

#COPY app.py /app.py
COPY . /app

EXPOSE 8000
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']