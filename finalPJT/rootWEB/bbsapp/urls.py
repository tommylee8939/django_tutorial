from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('main/', views.main , name='main'),

    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register , name='register'),

    # post
    path('bbs_list/', views.list , name='list'),
    path('bbs_registerForm/', views.bbsForm, name='bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name='bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name='bbs_read'),
    # path('bbs_read/', views.bbsRead, name='bbs_read'),
    path('bbs_delete/', views.bbsDelete, name='bbs_delete'),
    path('bbs_adjust/', views.bbsAdjust, name='bbs_adjust'),
    path('bbs_search/', views.bbsSearch, name='bbs_search'),
]