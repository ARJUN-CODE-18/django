# editor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_entry, name='create_entry'),
    path('entries/', views.show_entries, name='show_entries'),
]
