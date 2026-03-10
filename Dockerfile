FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем весь код приложения
COPY . .

# Команда запуска с watchfiles для разработки
# CMD ["watchfiles", "python main.py", "app"]
CMD ["watchfiles", "python main.py", "app", "main.py"]