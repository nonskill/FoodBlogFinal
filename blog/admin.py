from django.contrib import admin
from .models import Post
from .models import Highlight
from .models import Event

admin.site.register(Post)
admin.site.register(Highlight)
admin.site.register(Event)