# Generated by Django 4.0.5 on 2023-07-13 18:09

from django.db import migrations, models
import django.db.models.deletion
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]
