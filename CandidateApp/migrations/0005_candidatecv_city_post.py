# Generated by Django 2.2.6 on 2019-11-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0004_auto_20191104_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatecv',
            name='city_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
