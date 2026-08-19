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

    def __str__(self):
        return f"Inspection for {self.assignment.property.property_code} on {self.inspection_date}"

    class Meta:
        verbose_name_plural = "Inspection Details"    

class InspectionPhoto(models.Model):
    PHOTO_CATEGORY_CHOICES = [
        ("access_road", "Access Road / Entrance"),
        ("subject_property", "Subject Property"),
        ("adjacent_property", "Adjacent Property"),
        ("map_default", "Location Map — Default/Terrain View"),
        ("map_satellite", "Location Map — Satellite View"),
        ("map_directions", "Location Map — Direction from Nearest City/Landmark"),
        ("other", "Other"),
    ]

    inspection = models.ForeignKey(
        InspectionDetails, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to="inspection_photos/%Y/%m/")
    category = models.CharField(max_length=30, choices=PHOTO_CATEGORY_CHOICES)
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.inspection}"

class LandDetails(models.Model):
    inspection = models.OneToOneField(
        InspectionDetails, on_delete=models.CASCADE, related_name="land_details"
    )
    land_use = models.CharField(max_length=100)
    topography = models.CharField(max_length=100, blank=True, null=True)
    shape = models.CharField(max_length=100, blank=True, null=True)
    road_frontage = models.CharField(max_length=100, blank=True, null=True)
    accessibility = models.CharField(max_length=100, blank=True, null=True)
    utilities = models.CharField(max_length=255, blank=True, null=True)
    zoning = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Land details for {self.inspection}"

    class Meta:
        verbose_name_plural = "Land Details"


class BuildingDetails(models.Model):
    CONSTRUCTION_STATUS_CHOICES = [
        ("planned", "Planned"),
        ("under_construction", "Under Construction"),
        ("complete", "Complete"),
    ]

    inspection = models.OneToOneField(
        InspectionDetails, on_delete=models.CASCADE, related_name="building_details"
    )
    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_type = models.CharField(max_length=100)
    occupancy = models.CharField(max_length=100, blank=True, null=True)
    construction_status = models.CharField(max_length=30, choices=CONSTRUCTION_STATUS_CHOICES, default="complete")
    year_built = models.PositiveIntegerField(blank=True, null=True)
    number_of_storeys = models.PositiveIntegerField(default=1)
    plinth_area = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text="Plinth area in square metres"
    )
    finishes = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)

    @property
    def plinth_area_sqft(self):
        if self.plinth_area is not None:
            return round(self.plinth_area * 10.7639, 2)
        return None

    def __str__(self):
        return f"Building details for {self.inspection}"

    class Meta:
        verbose_name_plural = "Building Details"


class FloorDetails(models.Model):
    building = models.ForeignKey(
        BuildingDetails, on_delete=models.CASCADE, related_name="floors"
    )
    floor_label = models.CharField(max_length=50, help_text="e.g. Ground, 1st, Mezzanine")
    floor_order = models.PositiveIntegerField(help_text="Used for sorting floors top to bottom")
    floor_use = models.CharField(max_length=100, blank=True, null=True)
    floor_area = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ["floor_order"]
        verbose_name_plural = "Floor Details"

    def __str__(self):
        return f"{self.floor_label} - {self.building}"


class UnitDetails(models.Model):
    OCCUPANCY_STATUS_CHOICES = [
        ("vacant", "Vacant"),
        ("occupied", "Occupied"),
        ("under_renovation", "Under Renovation"),
    ]

    floor = models.ForeignKey(
        FloorDetails, on_delete=models.CASCADE, related_name="units"
    )
    unit_number = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=100, help_text="e.g. 1-bedroom, office, retail")
    unit_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    occupancy_status = models.CharField(max_length=30, choices=OCCUPANCY_STATUS_CHOICES, default="vacant")

    def __str__(self):
        return f"Unit {self.unit_number} - {self.floor}"

    class Meta:
        verbose_name_plural = "Unit Details"        

class ValuationResult(models.Model):
    assignment = models.OneToOneField(
        ValuationAssignment, on_delete=models.CASCADE, related_name="result"
    )
    market_value = models.DecimalField(max_digits=15, decimal_places=2)
    mortgage_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    insurance_value = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True,
        help_text="Reinstatement/insurance value"
    )
    reconciliation_notes = models.TextField(
        blank=True, null=True,
        help_text="Explanation of how the values were reached, especially if multiple methods were combined"
    )
    valuation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Valuation for {self.assignment.property.property_code} - {self.market_value}"

class CostApproachDetail(models.Model):
    valuation_result = models.ForeignKey(
        ValuationResult, on_delete=models.CASCADE, related_name="cost_approach"
    )
    construction_rate = models.DecimalField(max_digits=12, decimal_places=2)
    depreciation_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    computed_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Cost approach for {self.valuation_result}"


class IncomeApproachDetail(models.Model):
    valuation_result = models.ForeignKey(
        ValuationResult, on_delete=models.CASCADE, related_name="income_approach"
    )
    gross_income = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    cap_rate = models.DecimalField(max_digits=5, decimal_places=2)
    computed_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Income approach for {self.valuation_result}"