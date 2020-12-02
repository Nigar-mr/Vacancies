# Generated by Django 2.2.6 on 2019-11-29 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0038_auto_20191129_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepost',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 29, 11, 20, 26, 230601)),
        ),
        migrations.AlterField(
            model_name='candidatepost',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='CompanyApp.SkillsModel'),
        ),
    ]