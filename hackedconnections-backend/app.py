from flask import Flask, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from config import MONGO_URI
import os

# Import blueprints
from routes.auth import auth_bp
from routes.teams import teams_bp

# Path to your frontend directory
frontend_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))

# Create Flask app
app = Flask(__name__, static_folder=frontend_folder, static_url_path="")
CORS(app)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.get_database()
app.config['DB'] = db

# Register API routes
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(teams_bp, url_prefix="/api/teams")

# Serve the frontend index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve static assets (JS, CSS, images, etc.)
@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)
