from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Connects root URL to home view
]
