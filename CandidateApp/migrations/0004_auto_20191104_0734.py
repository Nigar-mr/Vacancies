# Generated by Django 2.2.6 on 2019-11-04 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0003_citymodel_countrymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatecv',
            name='location',
        ),
        migrations.AddField(
            model_name='candidatecv',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CityModel'),
        ),
        migrations.AddField(
            model_name='candidatecv',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CountryModel'),
        ),
    ]
