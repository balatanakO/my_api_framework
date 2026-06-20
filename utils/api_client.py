# utils/api_client.py
# 服务员，负责跑腿送请求

import requests
import time
from utils.logger import logger

class FuWuYuan:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        if token:
            self.headers = {"Authorization": f"Bearer {token}"}
        else:
            self.headers = {}

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        start = time.time()
        try:
            resp = requests.post(url, json=data, headers=headers or self.headers)
            cost = (time.time() - start) * 1000
            logger.info(f"POST | {url} | {resp.status_code} | {cost:.0f}ms")
            return resp
        except requests.exceptions.RequestException as e:
            cost = (time.time() - start) * 1000
            logger.error(f"POST | {url} | 失败 | {cost:.0f}ms | {e}")
            return None

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        start = time.time()
        try:
            resp = requests.get(url, params=params, headers=headers or self.headers)
            cost = (time.time() - start) * 1000
            logger.info(f"GET  | {url} | {resp.status_code} | {cost:.0f}ms")
            return resp
        except requests.exceptions.RequestException as e:
            cost = (time.time() - start) * 1000
            logger.error(f"GET  | {url} | 失败 | {cost:.0f}ms | {e}")
            return None
