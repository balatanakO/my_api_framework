# test_cases/test_login.py
# 考官：测登录

import pytest
from config.config import Config
from utils.api_client import FuWuYuan


@pytest.mark.parametrize("username,password,expected_status,expected_msg", [
    ("admin", "123456", 200, "登录成功"),
    ("admin", "wrong", 401, "密码错误"),
    ("ghost", "123456", 404, "用户不存在"),
    ("", "123456", 400, "字段缺失"),
    ("admin", "", 400, "字段缺失"),
])
def test_login(base_url, username, password, expected_status, expected_msg):
    fwy = FuWuYuan(base_url)
    resp = fwy.post("/login", data={
        "username": username,
        "password": password
    })
    assert resp.status_code == expected_status
    assert resp.json()["msg"] == expected_msg
