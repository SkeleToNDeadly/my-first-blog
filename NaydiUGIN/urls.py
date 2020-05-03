from django.urls import path
from . import views
urlpatterns = [
	path('', views.ugh, name ='ugh'),

]
