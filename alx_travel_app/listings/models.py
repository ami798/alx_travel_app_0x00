#!/usr/bin/env python3
"""Models for travel app"""

from django.db import models


class Listing(models.Model):
    """Represents a travel listing"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Booking model linked to a listing"""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking for {self.guest_name} at {self.listing.title}"


class Review(models.Model):
    """Review model linked to a listing"""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.reviewer_name} - {self.rating}/5"
