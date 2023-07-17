# Generated by Django 4.0.5 on 2023-07-17 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_location_alter_profile_photo'),
        ('main', '0002_listing_brand_listing_color_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('ford', 'Ford'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('jeep', 'Jeep'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], default=None, max_length=24),
        ),
        migrations.CreateModel(
            name='LikedListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]