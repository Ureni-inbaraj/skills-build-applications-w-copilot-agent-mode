from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30),
            Activity.objects.create(user=users[1], type='cycle', duration=45),
            Activity.objects.create(user=users[2], type='swim', duration=25),
            Activity.objects.create(user=users[3], type='yoga', duration=60),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes'),
            Workout.objects.create(name='Strength Training', description='Strength for superheroes'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
