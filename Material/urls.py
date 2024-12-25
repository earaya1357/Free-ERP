from django.urls import path
from . import views

urlpatterns = [
    path('FreeERPHome', views.home, name='home'),
    path('Inventory', views.inventory, name='inventory'),
    path('Suppliers', views.suppliers, name='suppliers'),
    path('Organizations', views.organizations, name='organizations'),
    path('Admin', views.admin, name='admin'),
    path('Users', views.users, name='users'),
    path('Projects', views.projects, name='projects'),
    path('Parts', views.parts, name='parts'),
    # path('Companies', views.companies, name='companies'),
    # path('Orders', views.orders, name='orders'),
    # path('Logout', views.logout, name='logout'),
    # path('Login', views.login, name='login'),
    # path('Profile', views.profile, name='profile'),
]