# Generated by Django 3.0.3 on 2020-03-29 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pscraper', '0002_auto_20200328_2107'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seller',
            unique_together=set(),
        ),
    ]