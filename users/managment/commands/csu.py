import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            first_name="bers",
            last_name="umar",
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Bers234')
        user.save()