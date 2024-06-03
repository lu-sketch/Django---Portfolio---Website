from django.urls import path
from . import views

"""creating the urls for the blog pages"""

# the blog app the url routes for this site

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='blog_list'),
    path('<int:post_id>/', views.post_detail, name='blog_detail'),
]
