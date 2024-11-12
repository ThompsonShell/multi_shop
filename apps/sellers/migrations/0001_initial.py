# Generated by Django 5.1.1 on 2024-11-07 21:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='rating')),
                ('seller_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='SellerSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social', models.PositiveSmallIntegerField(choices=[(0, 'Instagram'), (1, 'Telegram'), (2, 'Twitter'), (3, 'YouTube')])),
                ('social_media', models.URLField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('language', models.CharField(choices=[('en', 'En'), ('ru', 'Ru'), ('uz', 'Uz')], max_length=10, verbose_name='language')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller')),
            ],
        ),
    ]
