# Generated by Django 2.2.6 on 2019-11-13 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_auto_20191103_1539'),
        ('CompanyApp', '0017_aboutcomp_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcomp',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.CategoryModel'),
        ),
    ]