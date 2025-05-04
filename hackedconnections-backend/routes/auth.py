from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    db = current_app.config['DB']
    if db.users.find_one({"email": data["email"]}):
        return jsonify({"error": "Email already exists"}), 400

    hashed_pw = generate_password_hash(data["password"])
    user = {
        "name": data["name"],
        "email": data["email"],
        "password": hashed_pw,
        "skills": [],
        "projects": [],
        "achievements": [],
        "profile": {}
    }
    db.users.insert_one(user)
    return jsonify({"message": "User registered successfully"})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    db = current_app.config['DB']
    user = db.users.find_one({"email": data["email"]})
    if user and check_password_hash(user["password"], data["password"]):
        user["_id"] = str(user["_id"])
        del user["password"]
        return jsonify(user)
    return jsonify({"error": "Invalid credentials"}), 401
