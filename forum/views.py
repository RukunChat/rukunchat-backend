from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Forum, ForumResponse
from .forms import ForumForm, ForumResponseForm

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

@login_required(login_url='/auth/login/')
def reply_forum(request, forum_id):
    forum = Forum.objects.get(id=forum_id)

    if request.method == 'POST':
        form = ForumResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.forum = forum
            response.responder = request.user
            response.save()

            forum.num_responses += 1
            forum.save()

            return redirect('forum:show_all_forum')
    else:
        form = ForumResponseForm()

    context = {
        'form': form,
        'forum': forum,
    }
    return render(request, 'reply_forum.html', context)

@login_required(login_url='/auth/login/')
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    responses = forum.responses.all()

    context = {
        'forum': forum,
        'responses': responses
    }
    return render(request, 'forum_detail.html', context)