from django.urls import path
from myportfolio import views

app_name = 'myportfolio'
urlpatterns = [
    # Url for index page
    path('', views.index, name='index'),
    # Url for single project detail
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
]