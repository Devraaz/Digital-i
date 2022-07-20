from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')

    
]
