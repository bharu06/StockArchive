from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        call_command('loaddata', 'super_user')
        # Fix the passwords of fixtures[hashing is not done when inserted from fixtures]
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()