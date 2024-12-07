from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Booking
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# View for Homepage
def homepage(request):
    search_query = request.GET.get('search', '')

    if search_query:
        properties = Property.objects.filter(location__icontains=search_query)
    else:
        properties = Property.objects.all()

    return render(request, 'rentalapp/homepage.html', {'properties': properties})

# View for displaying properties
def property_list(request):
    # Fetch all properties from the database
    properties = Property.objects.all()

    # Pass properties to the template
    return render(request, 'rentalapp/property_list.html', {'properties': properties})

# View for displaying property details
def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)  # Fetch property by id
    return render(request, 'rentalapp/property_details.html', {'property': property})


# View for booking a property

def book_property(request, id):
    property = get_object_or_404(Property, id=id)

    if request.method == "POST":
        # Debug: Print request.POST
        print("Form submitted: ", request.POST)

        name = request.POST.get("name")
        email = request.POST.get("email")
        booking_date=request.POST.get("booking_date")

        # Check if all fields are received correctly
        print("Name:", name, "Email:", email, "booking_date:",booking_date)

        if name and email and booking_date:
            # Example saving logic (ensure you have a Booking model or database logic implemented)
            Booking.objects.create(
                property=property,
                name=name,
                email=email,
                booking_date=booking_date,
            )

            messages.success(request, f"Booking for {property.title} has been submitted successfully!")
            return redirect('property_detail', property_id=id)
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'rentalapp/book_property.html', {'property': property})
def services(request):
    return render(request, 'rentalapp/services.html')