# run.py
# 一键运行所有用例

import pytest

if __name__ == "__main__":
    pytest.main([
        "test_cases/",
        "-v",
        "--html=reports/report.html",
        "--self-contained-html"
    ])
