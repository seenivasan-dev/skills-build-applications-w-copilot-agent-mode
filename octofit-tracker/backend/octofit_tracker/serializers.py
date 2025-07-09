from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField()
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField()
    activity = serializers.CharField()
    duration = serializers.IntegerField()
    date = serializers.CharField()

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()
