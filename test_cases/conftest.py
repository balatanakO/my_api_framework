# test_cases/conftest.py
# 食材桌，pytest 启动先跑这个

import pytest
import subprocess
import time
from config.config import Config
from utils.api_client import FuWuYuan


@pytest.fixture(scope="session")
def base_url():
    """食材①：后厨地址"""
    hou_chu = subprocess.Popen(["python", "app.py"])
    time.sleep(1)
    yield Config.BASE_URL
    hou_chu.kill()


@pytest.fixture(scope="session")
def token(base_url):
    """食材②：登录拿 token"""
    fwy = FuWuYuan(base_url)
    resp = fwy.post("/login", json_data={
        "username": Config.TEST_USER,
        "password": Config.TEST_PASS
    })
    return resp.json()["token"]
