import logging
import requests
import yaml
from logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self):
        with open("config.yaml") as f:
            self.data = yaml.safe_load(f)

    def get_posts(self, owner, token):
        header = {"X-Auth-Token": token}
        res = requests.get(self.data["address"] + "api/posts", params={"owner": owner}, headers=header)
        return res.json()

    def create_post(self, token, post_data):
        header = {"X-Auth-Token": token}
        res = requests.post(self.data["address"] + "api/posts", headers=header, data=post_data)
        return res
