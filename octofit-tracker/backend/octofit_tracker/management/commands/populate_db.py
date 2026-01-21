from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Delete existing data (delete individually to avoid ObjectId hash issues)
        for model in [Activity, Workout, Leaderboard, User, Team]:
            for obj in model.objects.filter(id__isnull=False):
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel, is_superhero=True),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc, is_superhero=True),
            User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc, is_superhero=True),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc, is_superhero=True),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Cycling', duration=45, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        w1.suggested_for.set(users[:3])  # Marvel
        w2.suggested_for.set(users[3:])  # DC

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=300)
        Leaderboard.objects.create(team=dc, total_points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
