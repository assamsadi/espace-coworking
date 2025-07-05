
from django.urls import path
from .views import ReservationViews
reservationViews = ReservationViews()


urlpatterns = [
    path('create/', reservationViews.create_page , name="create_page"),
    path('list/', reservationViews.list_reservation , name="list_reservation"),
    path('up/', reservationViews.upi , name="upi"),
    path('set-time/<str:id>' , reservationViews.go_to_time , name="go_to_menu"),
    path('menu' , reservationViews.go_to_menu , name="go_to_menu_init"),
    path('timezome' , reservationViews.go_to_timezone , name="go_to_timezone"),
    path('facture' , reservationViews.go_to_facture , name="go_to_facture"),
    path('set-service-equip' , reservationViews.go_to_service_equipment , name="go_to_service_equipment"),
    path('add-equipment/<str:id>' , reservationViews.add_equipment , name="add_equipment"),
    path('delete-equipment/<str:i>' , reservationViews.delete_equipment , name="delete_equipment"),
    path('add-service/<str:id>' , reservationViews.add_service , name="add_service"),
    path('delete-service/<str:i>' , reservationViews.delete_service , name="delete_service"),
    path('upload_billet' , reservationViews.updoade_billet , name="updoade_billet"),
]