# Generated by Django 2.2.6 on 2019-11-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0014_companyvacancy_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysettings',
            name='profile_pict',
        ),
    ]