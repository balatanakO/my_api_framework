# app.py
# 后厨，处理请求

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "字段缺失"}), 400

    if username == "admin" and password == "123456":
        return jsonify({"token": "abc123", "msg": "登录成功"})
    elif username == "admin" and password != "123456":
        return jsonify({"msg": "密码错误"}), 401
    else:
        return jsonify({"msg": "用户不存在"}), 404


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "字段缺失"}), 400

    return jsonify({"username": username, "msg": "注册成功"})


@app.route("/user/<username>", methods=["GET"])
def get_user(username):
    return jsonify({"username": username, "email": f"{username}@test.com"})


if __name__ == "__main__":
    app.run(debug=True)
