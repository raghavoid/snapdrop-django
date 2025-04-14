from django.core.management.base import BaseCommand
from app.models import Login

class Command(BaseCommand):
    help = 'Create a staff user'

    def handle(self, *args, **kwargs):
        email = 'raghav2562.beai24@chitkara.edu.in'
        password = 'raghav@2969'

        if not Login.objects.filter(email=email).exists():
            staff_user = Login.objects.create_user(email=email, password=password)
            staff_user.is_staff = True
            staff_user.save()
            self.stdout.write(self.style.SUCCESS(f'Staff user {email} created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'User with email {email} already exists.'))