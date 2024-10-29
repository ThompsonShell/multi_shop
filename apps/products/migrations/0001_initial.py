# Generated by Django 5.1.1 on 2024-10-25 21:50

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('avg_rating', models.DecimalField(decimal_places=1, default=Decimal('0'), editable=False, max_digits=10)),
                ('comments_count', models.DecimalField(decimal_places=0, default=Decimal('0'), editable=False, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Enter in USD', max_digits=5)),
                ('old_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('UZS', 'UZS'), ('RUB', 'RUB')], default='USD', max_length=5)),
                ('short_description', models.CharField(max_length=250)),
                ('long_description', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_image', models.ImageField(upload_to='products/images/%Y/%m/%d/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/images/%Y/%m/%d/')),
                ('ordering_number', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
