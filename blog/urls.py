from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # Url for blog index page
    path("blog_index/", views.blog_index, name='blog_index'),
    # Url for blog detail page
    path('blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    # Url for blog category page
    path('blog_category/<category>/', views.blog_category, name='blog_category')
]