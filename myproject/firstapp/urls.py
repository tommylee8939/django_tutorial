from django.urls import path

from . import views

urlpatterns = [
    path('',views.index)   # root url 이 되는거지
]


