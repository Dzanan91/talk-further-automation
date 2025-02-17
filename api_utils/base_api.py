import requests
from config.config import BASE_API_URL 


class BaseAPI:
    def __init__(self, base_url: str = BASE_API_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, endpoint: str, json: dict, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json, **kwargs)

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)
