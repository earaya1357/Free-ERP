from django.urls import path
from . import views

urlpatterns = [
    path('FreeERPHome', views.home, name='home'),
    path('Inventory', views.inventory, name='inventory'),
    path('Suppliers', views.suppliers, name='suppliers'),
    path('Organizations', views.organizations, name='organizations'),
    path('Admin', views.admin, name='admin'),
]