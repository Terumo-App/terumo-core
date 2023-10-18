FROM python:3.10.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY /api/ /app/


CMD ["python", "main.py", "--reload=False"]