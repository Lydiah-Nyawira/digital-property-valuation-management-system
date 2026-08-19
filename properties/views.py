from django.shortcuts import render, redirect
from .forms import PropertyForm

def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/create_property.html', {'form': form})

def map_test(request):
    return render(request, 'properties/map_test.html')