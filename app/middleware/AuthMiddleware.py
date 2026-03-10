from rich import print
from app.web_api.AdminApiClient import AdminApiClient
from app.config import config

class AuthMiddleware:
    def __init__(self):
        self.apiClient = AdminApiClient()
        pass

    async def check_auth(self, user):
        # I need to check user in redis and if it has return true otherwise check in API
        await self.apiClient.check_user_access(user)

    async def register(self, user):
        result = await self.apiClient.register_user(user)
        return result