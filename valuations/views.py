from django.shortcuts import render
from .models import ValuationAssignment

def assignment_list(request):
    assignments = ValuationAssignment.objects.select_related('property', 'client').all()
    return render(request, 'valuations/assignment_list.html', {'assignments': assignments})
