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
    land_size = models.DecimalField(max_digits=12, decimal_places=2, help_text="Size in acres/hectares")
    property_user = models.CharField(max_length=100, blank=True, null=True)
    property_tenure = models.CharField(max_length=20, choices=TENURE_CHOICES)
    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_code} - {self.location}"

    class Meta:
        verbose_name_plural = "Properties"


class LandDetails(models.Model):
    """
    Land-specific attributes for a Property. One-to-one: a
    property has at most one land details record.
    """

    property = models.OneToOneField(
        Property, on_delete=models.CASCADE, related_name="land_details"
    )
    land_use = models.CharField(max_length=100)
    topography = models.CharField(max_length=100, blank=True, null=True)
    shape = models.CharField(max_length=100, blank=True, null=True)
    road_frontage = models.CharField(max_length=100, blank=True, null=True)
    accessibility = models.CharField(max_length=100, blank=True, null=True)
    utilities = models.CharField(max_length=255, blank=True, null=True)
    zoning = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Land details for {self.property.property_code}"

    class Meta:
        verbose_name_plural = "Land Details"    

class BuildingDetails(models.Model):
    """
    Building-specific attributes for a Property. One-to-one: a
    property has at most one building details record (a property
    with multiple physically separate buildings would need
    separate Property records, or this can be extended to FK
    later if that turns out to be a real requirement).
    """

    CONSTRUCTION_STATUS_CHOICES = [
        ("planned", "Planned"),
        ("under_construction", "Under Construction"),
        ("complete", "Complete"),
    ]

    property = models.OneToOneField(
        Property, on_delete=models.CASCADE, related_name="building_details"
    )
    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_type = models.CharField(max_length=100)
    occupancy = models.CharField(max_length=100, blank=True, null=True)
    construction_status = models.CharField(
        max_length=30, choices=CONSTRUCTION_STATUS_CHOICES, default="complete"
    )
    year_built = models.PositiveIntegerField(blank=True, null=True)
    number_of_storeys = models.PositiveIntegerField(default=1)
    plinth_area = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    finishes = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Building details for {self.property.property_code}"

    class Meta:
        verbose_name_plural = "Building Details"    

class FloorDetails(models.Model):
    """
    An individual floor within a building. FK back to
    BuildingDetails — a building has many floors.
    """

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
        return f"{self.floor_label} - {self.building.property.property_code}"


class UnitDetails(models.Model):
    """
    An individual unit (apartment, office, shop) within a floor.
    FK back to FloorDetails — a floor has many units.
    """

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
    occupancy_status = models.CharField(
        max_length=30, choices=OCCUPANCY_STATUS_CHOICES, default="vacant"
    )

    def __str__(self):
        return f"Unit {self.unit_number} - {self.floor}"

    class Meta:
        verbose_name_plural = "Unit Details"    