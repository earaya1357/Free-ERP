from django.urls import path
from . import views

urlpatterns = [
    path('MaterialsHome', views.home)
]