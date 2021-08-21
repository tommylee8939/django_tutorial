from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('main/', views.main ),
    path('script_page/', views.scriptIndex ),
    path('idChkAjax/',   views.idChkAjax),
    path('static/',views.staticFun),
    path('navbar/',views.navFun),
    path('bootstrap/', views.bootFun),

]