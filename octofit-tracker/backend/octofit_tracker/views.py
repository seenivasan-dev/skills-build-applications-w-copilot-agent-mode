from django.http import JsonResponse
from django.conf import settings
import socket
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

# Helper to get codespace name from environment or fallback
import os
def get_codespace_url():
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        return f"https://{codespace}-8000.app.github.dev"
    return None


def api_root(request):
    codespace_url = get_codespace_url()
    urls = {
        "local": "http://localhost:8000/",
        "codespace": codespace_url or "[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
    }
    return JsonResponse({"api": "OctoFit API Root", "urls": urls})

# MongoDB connection helper
client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def users_api(request):
    users = list(db.users.find({}, {'_id': 0}))
    return Response(UserSerializer(users, many=True).data)

@api_view(['GET'])
def teams_api(request):
    teams = list(db.teams.find({}, {'_id': 0}))
    return Response(TeamSerializer(teams, many=True).data)

@api_view(['GET'])
def activities_api(request):
    activities = list(db.activity.find({}, {'_id': 0}))
    return Response(ActivitySerializer(activities, many=True).data)

@api_view(['GET'])
def leaderboard_api(request):
    leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
    return Response(LeaderboardSerializer(leaderboard, many=True).data)

@api_view(['GET'])
def workouts_api(request):
    workouts = list(db.workouts.find({}, {'_id': 0}))
    return Response(WorkoutSerializer(workouts, many=True).data)
