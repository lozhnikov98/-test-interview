from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', my_view, name='my-view'),
    path('allwords', load, name='allwords')
]