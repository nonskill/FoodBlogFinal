from django import forms
from .models import Post
from .models import Highlight
from .models import Event

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'cover', 'text', 'published_date')

class HighlightForm(forms.ModelForm):

    class Meta:
        model = Highlight
        fields = ('author', 'title', 'cover', 'text', 'published_date')

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('author', 'title', 'cover', 'location', 'text', 'date', 'time')