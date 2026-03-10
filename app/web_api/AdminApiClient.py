import httpx
from typing import Optional, Dict, Any
from rich import print
from app.config import config

class AdminApiClient:
    def __init__(self):
        print(config.admin_api_url)
        self.client = httpx.AsyncClient(base_url=config.admin_api_url)

    async def register_user(self, user_data):
        headers = {
            "X-API-KEY": config.admin_api_key,
            "Accept": "application/json"
        }
        payload = user_data.model_dump()
        try:
            response = await self.client.post("/telegram/register", json=payload, headers=headers)
            return response.status_code in (200, 201)
        except Exception as e:
            print(f"Ошибка при регистрации в API: {e}")
            return False

    async def check_user_access(self, user):
        headers = {
            "X-API-KEY": config.admin_api_key,
            "Accept": "application/json"
        }
        try:
            response = await self.client.get(f"/telegram/user/{user.id}")
            return response.status_code == 200
        except Exception as e:
            print(f"Ошибка при проверке доступа в API: {e}")
            return False

    async def close(self):
        await self.client.aclose()

