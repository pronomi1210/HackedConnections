from flask import Blueprint, request, jsonify, current_app

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/', methods=['POST'])
def create_team():
    data = request.json
    db = current_app.config['DB']
    db.teams.insert_one(data)
    return jsonify({"message": "Team created successfully"})

@teams_bp.route('/', methods=['GET'])
def list_teams():
    db = current_app.config['DB']
    teams = list(db.teams.find())
    for team in teams:
        team["_id"] = str(team["_id"])
    return jsonify(teams)
