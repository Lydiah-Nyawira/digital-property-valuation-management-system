from django import forms
from .models import ValuationAssignment, InspectionDetails, ValuationResult, ComparableSale

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

class ComparableSaleForm(forms.ModelForm):
    class Meta:
        model = ComparableSale
        fields = [
            "location",
            "sale_price",
            "sale_date",
            "land_size",
            "adjustment_percent",
            "notes",
        ]
        widgets = {
            "sale_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }        