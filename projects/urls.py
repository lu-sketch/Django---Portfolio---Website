from django.urls import path
from . import views


"""url routes for the project app."""

app_name = 'projects'

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
]
