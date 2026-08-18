from django.shortcuts import render, redirect, get_object_or_404
from .models import ValuationAssignment, InspectionDetails, ValuationResult
from .forms import ValuationAssignmentForm, InspectionForm, ValuationResultForm

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

def add_inspection(request, assignment_id):
    assignment = get_object_or_404(ValuationAssignment, id=assignment_id)
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            inspection.assignment = assignment
            inspection.save()
            return redirect('assignment_list')
    else:
        form = InspectionForm()
    return render(request, 'valuations/add_inspection.html', {'form': form, 'assignment': assignment})

def add_result(request, assignment_id):
    assignment = get_object_or_404(ValuationAssignment, id=assignment_id)
    if request.method == 'POST':
        form = ValuationResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.assignment = assignment
            result.save()
            return redirect('assignment_list')
    else:
        form = ValuationResultForm()
    return render(request, 'valuations/add_result.html', {'form': form, 'assignment': assignment})          