from django.contrib import admin

from .models import ValuationAssignment, InspectionDetails, ValuationResult

admin.site.register(ValuationAssignment)
admin.site.register(InspectionDetails)
admin.site.register(ValuationResult)