from django.urls import path
from .views import EquipmentView
from django.conf import settings
from django.conf.urls.static import static
equipmentView= EquipmentView()
urlpatterns =[
    path('add/', equipmentView.create_page , name ='equipment_create_page'),
    path('save/', equipmentView.save , name ='equipment_save'),
    path('list/', equipmentView.list_equipment , name ='equipment_list'),
    path('delete/<str:id>', equipmentView.delete_equipment , name ='equipment_delete'),
    path('edit/<str:id>', equipmentView.edit_page , name ='equipment_create_edit'),
    path('cancel/', equipmentView.cancel , name ='equipment_cancel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)