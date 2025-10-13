# Python образ
FROM python:3.11-slim

# Переменные окружение
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Рабочая директория
WORKDIR /app

# Системные зависимости
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Зависимости
COPY requirements.txt .

# Pytthon зависимости
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Статик и медиа директории
RUN mkdir -p /app/staticfiles /app/media

EXPOSE 8000
