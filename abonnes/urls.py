from django.urls import path
from . import views

urlpatterns =[
    path('admin/', views.crete_page_abo , name="page_abo") ,
    path('create/<str:ty>', views.crete_abo),
]