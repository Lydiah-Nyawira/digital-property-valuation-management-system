from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_client, name='create_client'),
]