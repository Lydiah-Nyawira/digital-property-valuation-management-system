from django import forms
from .models import ValuationAssignment, InspectionDetails

class ValuationAssignmentForm(forms.ModelForm):
    class Meta:
        model = ValuationAssignment
        fields = ['property', 'client', 'valuer', 'purpose', 'status']

class InspectionForm(forms.ModelForm):
    class Meta:
        model = InspectionDetails
        fields = ['inspection_date', 'inspected_by', 'condition', 'observations']