# utils/db_helper.py
# 数据库助手，帮你查数据库、改数据库

import sqlite3
from config.config import Config


class DBHelper:
    def __init__(self):
        """开门：连数据库"""
        self.conn = sqlite3.connect(Config.DB_PATH)
        self.cursor = self.conn.cursor()

    def query(self, sql):
        """查数据：SELECT 用这个"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        """改数据：INSERT / UPDATE / DELETE 用这个"""
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        """关门"""
        self.conn.close()
