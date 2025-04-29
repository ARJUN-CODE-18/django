from django.shortcuts import render, redirect
from .models import TheBookLost
from .forms import TheBookLostForm

def create_entry(request):
    if request.method == 'POST':
        form = TheBookLostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_entries')
    else:
        form = TheBookLostForm()
    return render(request, 'editor/create_entry.html', {'form': form})

def show_entries(request):
    entries = TheBookLost.objects.all()
    return render(request, 'editor/show_entries.html', {'entries': entries})
