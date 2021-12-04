from django.urls import path
from . import views

urlpatterns = [
    path('work/<int:pk>/', views.work_detail, name="app_detail"),
    path('', views.home, name="home"),
]