import os

from django.conf import settings

from django.core.management.base import BaseCommand
from django.template.context_processors import request

from django.utils.timezone import now
from jedi.inference.syntax_tree import operator_to_magic_method

from apps.abouts.models import About

from faker import Faker

fake = Faker()

RANDOM_CAT_IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
os.makedirs(os.path.join('/home/thompson/Desktop/multi_shop', 'salom/api'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("hello world")
        today = now().date()

        if not About.objects.exists():
            image_url = request(url=RANDOM_CAT_IMAGE_URL).json()[0]
            image_name = image_url.split('/')[-1]
            image_dir = settings.MEDIAD_ROOT + f'abouts/images/{today.year}/{today.month}/{today.day}/'
            filename = os.path.join(image_dir, image_name)
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)


            with open(filename, 'wb') as image:
                image.write(request.get(image_url).content)

            About.objects.create(
                title=fake.text(255),
                description=fake.text(250),
                image=fake.image()
            )