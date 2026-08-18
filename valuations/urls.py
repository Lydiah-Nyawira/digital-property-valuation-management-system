from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/create/', views.create_assignment, name='create_assignment'),
    path('assignments/<int:assignment_id>/inspection/', views.add_inspection, name='add_inspection'),
]