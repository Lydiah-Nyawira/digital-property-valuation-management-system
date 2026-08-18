from django.shortcuts import render, redirect
from .models import ValuationAssignment
from .forms import ValuationAssignmentForm

def assignment_list(request):
    assignments = ValuationAssignment.objects.select_related('property', 'client').all()
    return render(request, 'valuations/assignment_list.html', {'assignments': assignments})

def create_assignment(request):
    if request.method == 'POST':
        form = ValuationAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = ValuationAssignmentForm()
    return render(request, 'valuations/create_assignment.html', {'form': form})    