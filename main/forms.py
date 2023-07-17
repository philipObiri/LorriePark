from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = {
            "description",
            "brand",
            "model",
            "vin",
            "mileage",
            "color",
            "engine",
            "transmission",
            "image",
        }


