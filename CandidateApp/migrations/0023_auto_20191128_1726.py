# Generated by Django 2.2.6 on 2019-11-28 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0022_auto_20191128_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatepost',
            old_name='description',
            new_name='job_description',
        ),
    ]
