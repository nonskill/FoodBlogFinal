from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm # new
from .forms import HighlightForm #new
from .forms import EventForm #new
from .models import Post
from .models import Highlight
from .models import Event


def post_list(request):
    posts = Post.objects.order_by('-published_date')
    highlights = Highlight.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts, 'highlights': highlights})

def event_list(request):
    events = Event.objects.all
    return render(request, 'blog/events.html', {'events': events})

def events(request):
    events = Event.objects.all
    return render(request, 'blog/events.html', {'events': events})

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('post_list')

class CreateHighlightView(CreateView): # new
    model = Highlight
    form_class = HighlightForm
    template_name = 'highlight.html'
    success_url = reverse_lazy('post_list')

class CreateEventView(CreateView): # new
    model = Event
    form_class = EventForm
    template_name = 'event.html'
    success_url = reverse_lazy('events')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def highlight_detail(request, pk):
    highlight = get_object_or_404(Highlight, pk=pk)
    return render(request, 'blog/highlight_detail.html', {'highlight': highlight})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/event_detail.html', {'event': event})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def highlight_edit(request, pk):
    highlight = get_object_or_404(Highlight, pk=pk)
    if request.method == "POST":
        form = HighlightForm(request.POST, request.FILES, instance=highlight)
        if form.is_valid():
            highlight.published_date = timezone.now()
            highlight.save()
            return redirect('highlight_detail', pk=highlight.pk)
    else:
        form = HighlightForm(instance=highlight)
    return render(request, 'blog/highlight_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/event_edit.html', {'form': form})
