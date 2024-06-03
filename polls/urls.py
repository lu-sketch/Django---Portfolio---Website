from django.urls import path
from . import views

"""url routes for the login and register pages, when the user chooses
the polls app from the 'home' page."""


app_name = 'polls'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('polls/', views.poll_list, name='poll_list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
]



