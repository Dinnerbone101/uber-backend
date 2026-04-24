from django.urls import path
from .views import *

urlpatterns = [
    path('create-ride/', create_ride),
    path('start-ride/<int:ride_id>/', start_ride),
    path('complete-ride/<int:ride_id>/', complete_ride),
]