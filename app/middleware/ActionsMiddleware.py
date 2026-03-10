from rich import print
from app.web_api.AdminApiClient import AdminApiClient

class ActionsMiddleware:
    def __init__(self):
        self.api = AdminApiClient()
        pass

    def write_user_action(self, user, action):
        print({'action' : user})