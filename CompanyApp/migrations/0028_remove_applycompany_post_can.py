# Generated by Django 2.2.6 on 2019-11-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0027_applycompany_post_can'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applycompany',
            name='post_can',
        ),
    ]
