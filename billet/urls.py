from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.list_page_billet , name = 'list_page_billet'),
    path('upload/<str:id>', views.upload_pdf , name = 'upload_pdf'),
]