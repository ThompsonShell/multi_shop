# Generated by Django 5.1.1 on 2024-11-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('description_en', models.TextField(blank=True, max_length=255, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='abouts/images/%Y/%m/%d/')),
            ],
        ),
    ]
