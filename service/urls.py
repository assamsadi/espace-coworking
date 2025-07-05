from django.urls import path
from .views import ServiceViews
equipmentView= ServiceViews()
urlpatterns =[
    path('add/', equipmentView.create_page , name ='service_create_page'),
    path('save/', equipmentView.save , name ='service_save'),
    path('list/', equipmentView.list_equipment , name ='service_list'),
    path('delete/<str:id>', equipmentView.delete_equipment , name ='service_delete'),
    path('edit/<str:id>', equipmentView.edit_page , name ='service_create_edit'),
    path('cancel/', equipmentView.cancel , name ='service_cancel'),

]
