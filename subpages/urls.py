from django.urls import path
from . import views

urlpatterns = [
    path('<str:subpage_name>/', views.subpage_detail, name='subpage_detail'),
]