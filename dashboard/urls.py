from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.dashboard_page , name='dashboard_page'),
]