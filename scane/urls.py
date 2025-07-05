from django.urls import path
from .views import CardView
cardView = CardView()

urlpatterns = [
    path('equipment/<str:id>/', cardView.qr_page),
    path('to_reserve/<str:id>/', cardView.to_reserve , name="to_reserve"),
    path('to_done/<str:id>/', cardView.to_done , name="to_done"),
    path('e1/<str:id>/', cardView.uploud_pdf),
    path('up', cardView.up_up , name="up_up"),
    path('succes/', cardView.card_done , name="card_done"),
]