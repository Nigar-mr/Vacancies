# Generated by Django 2.2.6 on 2020-10-26 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0040_auto_20200506_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepost',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 26, 13, 51, 55, 703718)),
        ),
    ]