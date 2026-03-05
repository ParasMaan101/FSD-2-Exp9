from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from functools import wraps
import base64
import os

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")
jwt = JWTManager(app)

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({"message": "Authentication API Running Successfully"})


# =====================================================
# 1️⃣ BASIC AUTH (Authorization Header)
# =====================================================
@app.route("/basic-auth")
def basic_auth():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"message": "Authorization header missing"}), 401

    try:
        auth_type, credentials = auth_header.split()
        decoded = base64.b64decode(credentials).decode("utf-8")
        username, password = decoded.split(":")
    except Exception:
        return jsonify({"message": "Invalid Authorization format"}), 401

    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "Basic Authentication Successful"})
    else:
        return jsonify({"message": "Invalid Credentials"}), 401


# =====================================================
# 2️⃣ CUSTOM HEADER AUTH
# =====================================================
@app.route("/custom-auth")
def custom_auth():
    username = request.headers.get("username")
    password = request.headers.get("password")

    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "Custom Header Authentication Successful"})
    else:
        return jsonify({"message": "Invalid Credentials"}), 401


# =====================================================
# 3️⃣ JWT LOGIN
# =====================================================
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Missing JSON body"}), 400

    username = data.get("username")
    password = data.get("password")

    if username == USERNAME and password == PASSWORD:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"message": "Invalid Credentials"}), 401


# =====================================================
# 4️⃣ JWT PROTECTED ROUTE
# =====================================================
@app.route("/jwt-protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "JWT Authentication Successful",
        "logged_in_as": current_user
    })


# =====================================================
# RUN APP
# =====================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)