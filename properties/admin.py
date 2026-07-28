from django.contrib import admin
from .models import Property, LandDetails, BuildingDetails, FloorDetails, UnitDetails

admin.site.register(Property)
admin.site.register(LandDetails)
admin.site.register(BuildingDetails)
admin.site.register(FloorDetails)
admin.site.register(UnitDetails)