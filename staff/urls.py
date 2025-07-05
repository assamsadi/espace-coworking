from django.urls import path
from . import views
urlpatterns =[
    path("list", views.list_page , name="list_page_staff"),
    path("preparation/<str:id>", views.to_preparation, name="to_preparation"),
    path("done/<str:id>", views.to_prete, name="to_prete"),

]