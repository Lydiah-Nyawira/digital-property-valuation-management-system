from django.db import models
from django.conf import settings
from properties.models import Property
from clients.models import Client

class ValuationAssignment(models.Model):
    STATUS_CHOICES = [
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="valuation_assignments"
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="valuation_assignments"
    )
    valuer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="assignments"
    )
    purpose = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="e.g. Mortgage, Sale, Insurance, Rating"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="assigned")
    date_assigned = models.DateField(auto_now_add=True)
    date_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.property.property_code} - {self.status}"# Create your models here.