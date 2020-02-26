# Generated by Django 3.0.3 on 2020-02-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=31, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False, unique=True)),
                ('listing_id', models.CharField(max_length=255, unique=True)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('trim', models.CharField(max_length=255)),
                ('body_style', models.CharField(max_length=255)),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('first_date', models.DateField()),
                ('last_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('seller_id', models.IntegerField()),
            ],
        ),
    ]
