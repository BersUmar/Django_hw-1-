import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="umar-03@inbox.ru",
            first_name="umar-03",
            last_name="inbox.ru",
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Bers234')
        user.save()