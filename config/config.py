# config/config.py
# 所有会变的数字和字符串，全关在这里

class Config:
    # 后厨地址
    BASE_URL = "http://127.0.0.1:5000"
    DB_PATH = "data/test.db"

    # 超时时间（秒）
    TIMEOUT = 10

    # 测试账号
    TEST_USER = "admin"
    TEST_PASS = "123456"
