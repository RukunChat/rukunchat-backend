from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, ForumResponse
from .forms import ForumForm

@login_required(login_url='/auth/login/')
def show_all_forum(request):
    forums = Forum.objects.all()
    context = {
        'forums': forums
    }
    return render(request, 'show_all_forum.html', context)

@login_required(login_url='/auth/login/')
def add_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.creator = request.user
            forum.save()
            return redirect('forum:show_all_forum')
    else:
        form = ForumForm()

    context = {
        'form': form
    }
    return render(request, 'add_forum.html', context)
