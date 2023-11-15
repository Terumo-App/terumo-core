FROM python:3.10.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

ENV ON_CONTAINER=True

EXPOSE 8000

CMD ["python", "main.py", "--reload=False"]