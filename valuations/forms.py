from django import forms
from .models import ValuationAssignment, InspectionDetails, ValuationResult

class ValuationAssignmentForm(forms.ModelForm):
    class Meta:
        model = ValuationAssignment
        fields = ['property', 'client', 'valuer', 'purpose', 'status']

class InspectionForm(forms.ModelForm):
    class Meta:
        model = InspectionDetails
        fields = ['inspection_date', 'inspected_by', 'condition', 'observations']

class ValuationResultForm(forms.ModelForm):
    class Meta:
        model = ValuationResult
        fields = ['market_value', 'mortgage_value', 'insurance_value', 'reconciliation_notes']