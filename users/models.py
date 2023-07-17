from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
from .utils import user_directory_path

# Create your models here.


class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField(default="NY")
    zip_code = USZipCodeField(blank=True)

    def __str__(self):
        return f"Location {self.id}"


# Extending the built in User model
class Profile(models.Model):
    # a user can have one and only one profile :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=user_directory_path, null=True
    )  # Profile Picture is optional
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
