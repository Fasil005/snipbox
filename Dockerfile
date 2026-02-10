FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install uv
RUN uv pip install -r requirements.txt --system

COPY . .

RUN python manage.py collectstatic --noinput
