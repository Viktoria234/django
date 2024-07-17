from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.html_response, name='home')
]