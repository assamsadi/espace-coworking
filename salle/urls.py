from django.urls import path
from .views import SalleView
from django.conf import settings
from django.conf.urls.static import static
salleView= SalleView()
urlpatterns =[
    path('add/', salleView.create_page , name ='salle_create_page'),
    path('save/', salleView.save , name ='salle_save'),
    path('list/', salleView.list_salle , name ='salle_list'),
    path('delete/<str:id>', salleView.delete_salle , name ='salle_delete'),
    path('edit/<str:id>', salleView.edit_page , name ='salle_create_edit'),
    path('equipment-add/<str:equi>', salleView.add_equi , name ='add_equii'),
    path('equipment-delete/<str:equi>', salleView.delete_equi , name ='delete_equi'),
    path('cancel/', salleView.cancel , name ='salle_cancel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)