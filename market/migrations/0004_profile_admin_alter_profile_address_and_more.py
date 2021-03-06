# Generated by Django 4.0.6 on 2022-07-15 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='market',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
