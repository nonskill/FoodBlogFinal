from django.urls import path
from . import views
from .views import CreatePostView
from .views import CreateHighlightView
from .views import CreateEventView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.event_list, name='event_list'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('highlight/', CreateHighlightView.as_view(), name='add_highlight'),
    path('event/', CreateEventView.as_view(), name='add_event'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('highlight/<int:pk>/', views.highlight_detail, name='highlight_detail'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('highlight/<int:pk>/edit/', views.highlight_edit, name='highlight_edit'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('events/', views.events, name='events'),
]