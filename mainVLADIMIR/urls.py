
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ban, name = 'ban'),
]
