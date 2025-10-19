from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class OctofitModelsTest(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.user1 = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        self.user2 = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        self.activity = Activity.objects.create(user=self.user1, type='run', duration=30)
        self.workout = Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes')
        self.leaderboard = Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(self.user1.team.name, 'Marvel')
        self.assertEqual(self.user2.team.name, 'DC')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')
        self.assertEqual(self.activity.duration, 30)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Morning Cardio')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.team.name, 'Marvel')
        self.assertEqual(self.leaderboard.points, 100)
