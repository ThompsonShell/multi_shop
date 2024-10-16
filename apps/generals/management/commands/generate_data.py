import os
from random import random, randint, choice
from tkinter import image_names

import requests

from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand
from django.template.context_processors import request

from django.utils.timezone import now
from jedi.inference.syntax_tree import operator_to_magic_method

from apps.abouts.models import About

from faker import Faker

from apps.categories.models import Category
from apps.categories.views import category
from apps.generals.services import random_image_download
from apps.products.models import CURRENCY_CHOICES, Product

fake = Faker()


class Command(BaseCommand):

    @staticmethod
    def generate_about():
        today = now().date()
        django_filename = f'abouts/images/{today.year}/{today.month}/{today.day}/'
        # ===== check image ir for existing =====
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)

        if not About.objects.exists():
            image_name = random_image_download(image_dir)

            About.objects.create(
                title=fake.text(255),
                description=fake.text(250),
                image=os.path.join(django_filename, image_name)
            )

    @staticmethod
    def generate_product():
        today = now().date()
        django_filename = f'products/images/{today.year}/{today.month}/{today.day}/'
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)

        for cat_id in range(90):
            category = Category.objects.create(
                name=fake.text(250)
            )

            # ===== check image ir for existing =====
            image_name = random_image_download(image_dir)
            for i in range(10):
                print("=========")

            products = []
            for i in range(10):
                print("success")
                products.append(
                    Product(
                        title=fake.text(150),
                        price=randint(100, 100),
                        old_price=randint(100, 100),
                        currency=choice(CURRENCY_CHOICES)[0],
                        short_description=fake.text(250),
                        long_description=fake.text(10_000),
                        category_id=category.pk,
                        main_image=os.path.join(django_filename, image_name)
                    )
                )

        Product.objects.bulk_create(products)

    @transaction.atomic
    def handle(self, *args, **options):
        # ===== generate about model =====
        print(self.stdout.write(self.style.SUCCESS('Generating about data !')))
        self.generate_about()

        # ===== generate product model =====
        print(self.stdout.write(self.style.SUCCESS('Generating products data !')))
        self.generate_product()
        print(self.stdout.write(self.style.SUCCESS('Done')))
