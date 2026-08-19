from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_property, name='create_property'),
    path('map-test/', views.map_test, name='map_test'),
]