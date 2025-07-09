from django.core.management.base import BaseCommand
import pymongo

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data based on example (replace with actual data as needed)
        users = [
            {"email": "alice@example.com", "name": "Alice", "team": "Red", "age": 16},
            {"email": "bob@example.com", "name": "Bob", "team": "Blue", "age": 17},
            {"email": "carol@example.com", "name": "Carol", "team": "Red", "age": 15}
        ]
        teams = [
            {"name": "Red", "members": ["alice@example.com", "carol@example.com"]},
            {"name": "Blue", "members": ["bob@example.com"]}
        ]
        activities = [
            {"user": "alice@example.com", "activity": "Running", "duration": 30, "date": "2025-07-01"},
            {"user": "bob@example.com", "activity": "Cycling", "duration": 45, "date": "2025-07-02"},
            {"user": "carol@example.com", "activity": "Swimming", "duration": 25, "date": "2025-07-03"}
        ]
        leaderboard = [
            {"team": "Red", "points": 120},
            {"team": "Blue", "points": 90}
        ]
        workouts = [
            {"name": "Morning Run", "type": "Cardio", "duration": 30},
            {"name": "Strength Circuit", "type": "Strength", "duration": 40}
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
