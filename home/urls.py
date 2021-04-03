from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_bot', add_bot, name='add_bot'),
]
