from django.shortcuts import render
from .pagedown_editor.editor.forms import TheBookLostForm
from .models import TheBookLost

def editor_view(request):
    if request.method == 'POST':
        form = TheBookLostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TheBookLostForm()
    return render(request, 'editor/editor.html', {'form': form})

def all_posts(request):
    posts = TheBookLost.objects.all()
    return render(request, 'editor/all_post.html', {'posts': posts})
