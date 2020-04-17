from django.urls import path
from myportfolio import views

urlpatterns = [
    # Url for index page
    path('', views.index, name='index'),
]