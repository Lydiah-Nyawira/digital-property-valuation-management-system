from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title_number', 'property_code', 'location', 'county', 'sub_county',
                   'coordinates', 'land_size', 'property_user', 'property_tenure', 'ownership_type']