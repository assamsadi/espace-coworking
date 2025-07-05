from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-checkout-session/<str:id>', views.create_checkout_session, name='create_checkout_session'),
    path('create_checkout_abonne', views.create_checkout_abonne, name='create_checkout_abonne'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
