from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('main/', views.index),
    path('line/',views.line),
    path('bar/',views.bar)
]