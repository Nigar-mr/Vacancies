# Generated by Django 2.2.6 on 2019-11-28 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0027_auto_20191128_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatepost',
            name='date',
        ),
        migrations.AddField(
            model_name='candidatepost',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 28, 17, 52, 19, 665799)),
        ),
    ]