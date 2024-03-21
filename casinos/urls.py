from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('casino/<str:pk>/', views.casino, name="casino"),
]