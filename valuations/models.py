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
        return f"{self.property.property_code} - {self.status}"

class InspectionDetails(models.Model):
    CONDITION_CHOICES = [
        ("excellent", "Excellent"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("poor", "Poor"),
    ]

    assignment = models.OneToOneField(
        ValuationAssignment, on_delete=models.CASCADE, related_name="inspection"
    )
    inspection_date = models.DateField()
    inspected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="inspections"
    )
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    observations = models.TextField(blank=True, null=True, help_text="General notes from the inspection")
    photos_taken = models.BooleanField(default=False)

    def __str__(self):
        return f"Inspection for {self.assignment.property.property_code} on {self.inspection_date}"

class ValuationResult(models.Model):
    METHOD_CHOICES = [
        ("cost", "Cost Approach"),
        ("market", "Market/Sales Comparison Approach"),
        ("income", "Income Approach"),
    ]

    assignment = models.OneToOneField(
        ValuationAssignment, on_delete=models.CASCADE, related_name="result"
    )
    method_used = models.CharField(max_length=20, choices=METHOD_CHOICES)
    valuation_amount = models.DecimalField(max_digits=15, decimal_places=2)
    rate_used = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text="Rate per sqm/unit used in the calculation, if applicable"
    )
    valuation_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Valuation for {self.assignment.property.property_code} - {self.valuation_amount}"