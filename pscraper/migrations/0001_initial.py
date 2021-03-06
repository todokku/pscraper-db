# Generated by Django 3.0.3 on 2020-04-13 04:04

from django.db import migrations, models
import django.db.models.deletion


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
                ('address', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('listing_id', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('trim', models.CharField(blank=True, max_length=255, null=True)),
                ('body_style', models.CharField(blank=True, max_length=255, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('first_date', models.DateField()),
                ('last_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pscraper.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('price', models.FloatField(blank=True, null=True)),
                ('date', models.DateField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pscraper.Seller')),
            ],
        ),
    ]
