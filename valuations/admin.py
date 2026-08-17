from django.contrib import admin

from .models import ValuationAssignment, InspectionDetails, LandDetails, BuildingDetails, FloorDetails, UnitDetails, ValuationResult

admin.site.register(ValuationAssignment)
admin.site.register(InspectionDetails)
admin.site.register(LandDetails)
admin.site.register(BuildingDetails)
admin.site.register(FloorDetails)
admin.site.register(UnitDetails)
admin.site.register(ValuationResult)