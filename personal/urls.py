from django.urls import path
from . import views

"""the following paths are for the
about, contact and education html pages"""


app_name = 'personal'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]

