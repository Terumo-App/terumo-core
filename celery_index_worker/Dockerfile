FROM python:3.10.11-slim-bullseye
# ENV PYTHONUNBUFFERED=1

WORKDIR /app
# layer caching for faster builds
COPY requirements.txt /
RUN pip install --upgrade pip && pip install -r /requirements.txt

# RUN mkdir -p /app/file_storage

#COPY app.py /app.py
COPY . /app

USER root

# RUN mkdir -p ~/.cache/torch/hub/checkpoints/
# # don't do this in production - modify command to give permission to users who require it.
# RUN chmod -R 777 ~/.cache/torch/hub/checkpoints/ 

EXPOSE 8000
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
#ENTRYPOINT ['celery -A test_celery worker --loglevel=info']