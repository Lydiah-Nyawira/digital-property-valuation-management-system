from django import forms
from .models import ValuationAssignment

class ValuationAssignmentForm(forms.ModelForm):
    class Meta:
        model = ValuationAssignment
        fields = ['property', 'client', 'valuer', 'purpose', 'status']