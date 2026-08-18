from django.shortcuts import render, redirect
from .forms import ClientForm

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = ClientForm()
    return render(request, 'clients/create_client.html', {'form': form})
