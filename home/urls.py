from django.urls import path
from .views import *


urlspatterns = [
    path('',Home.as_view(),name='home')
]

