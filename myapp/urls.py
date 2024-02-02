from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('',index,name='index'),
    path('data/',data_view,name='dataview')
    
]