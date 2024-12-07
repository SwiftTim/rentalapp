from django.db import models


# Model for Property details
# models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='property_images/')  # Image field

    def __str__(self):
        return self.title



# Model for Booking details
class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    booking_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.property.title} by {self.name}"
