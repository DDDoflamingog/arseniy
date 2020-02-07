from django.contrib import admin
from django.urls import path
from med import views

urlpatterns = [
    path('', views.index, name='home'),

]