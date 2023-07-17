from django.shortcuts import render, redirect
from imp import reload
from .models import Listing
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter

# Create your views here.


def main_vew(request):
    return render(request, "views/main.html")


@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        "listing_filter": listing_filter,
    }
    return render(request, "views/home.html", context)


@login_required
def list_view(request):
    if request.method == "POST":
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if listing_form.is_valid and location_form.is_valid:
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f"{listing.model} : Listing posted successfully !"
                )
                return redirect("home")
            else:
                raise Exception()
        except Exception as e:
            print("Error Detail : ", e)
            messages.error(request, "An error occurred while posting the listing")

    elif request.method == "GET":
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(
        request,
        "views/list.html",
        {
            "listing_form": listing_form,
            "location_form": location_form,
        },
    )


@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(
            request,
            "views/listing.html",
            {
                "listing": listing,
            },
        )
    except Exception as e:
        messages.error(request, f"Invalid UID {id} was provided for listing.")
        return redirect("home")


@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == "POST":
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing)
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.success(request, f"Listing {id} updated successfully !")
                return redirect("home")
            else:
                messages.error("An error occurred while trying to edit the listing !")
                return reload()
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
    except Exception as e:
        messages.error(
            request, f"An error occurred while trying to access the application"
        )
    return render(
        request,
        "views/edit.html",
        {
            "listing_form": listing_form,
            "location_form": location_form,
        },
    )