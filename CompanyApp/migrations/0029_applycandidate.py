# Generated by Django 2.2.6 on 2019-11-29 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CompanyApp', '0028_remove_applycompany_post_can'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatee', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companyy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]