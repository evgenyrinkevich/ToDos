import json
from django.core.management.base import BaseCommand
from django.db import transaction

from users.models import User


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        users = load_from_json('users/fixtures/users.json')

        User.objects.all().delete()
        for user in users:
            pk = user.get('pk')
            item = user.get('fields')
            new_user = User(pk=pk, **item)
            new_user.save()

        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser(username='django', email='django@gb.ru', password='geekbrains')
