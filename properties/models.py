from django.db import models


class Property(models.Model):
    """
    The base entity representing a single piece of real estate —
    could be raw land, a standalone building, or a multi-unit
    development. LAND_DETAILS / BUILDING_DETAILS attach to this.
    """

    TENURE_CHOICES = [
        ("freehold", "Freehold"),
        ("leasehold", "Leasehold"),
    ]

    OWNERSHIP_CHOICES = [
        ("individual", "Individual"),
        ("company", "Company"),
        ("government", "Government"),
        ("trust", "Trust"),
    ]

    title_number = models.CharField(max_length=100, unique=True)
    property_code = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    land_size = models.DecimalField(max_digits=12, decimal_places=4, help_text="Land size in hectares")
    property_user = models.CharField(max_length=100, blank=True, null=True)
    property_tenure = models.CharField(max_length=20, choices=TENURE_CHOICES)
    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_code} - {self.location}"

    class Meta:
        verbose_name_plural = "Properties"