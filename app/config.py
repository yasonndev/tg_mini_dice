import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Вычисляем АБСОЛЮТНЫЙ путь к корню проекта
# Path(__file__) — это D:\...\bot-cozynest\app\config.py
# .parent — это папка app
# .parent.parent — это корень проекта D:\...\bot-cozynest
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    secret_key: str
    bot_username: str
    bot_token: str
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    admin_ids: list[int] = []

    # Указываем Pydantic точный абсолютный путь
    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding="utf-8",
        extra="ignore"
    )

# 2. Проверка для тебя (удалишь потом)
if not ENV_PATH.exists():
    print(f"❌ ОШИБКА: Файл не найден по пути {ENV_PATH}")

config = Settings()