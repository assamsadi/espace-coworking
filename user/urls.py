
from django.urls import path
from user.views import UserView
from django.conf import settings
from django.conf.urls.static import static
userView = UserView()
urlpatterns = [
    path('list/', userView.list_user, name='list_users'),
    path('create', userView.create_page, name='create_user_page'),
    path('delete/<str:id>', userView.delete_user, name='delete_user'),
    path('edit/<str:id>', userView.edit_page, name='edit_page'),
    path('cancel', userView.cancel, name='cancel'),
    path('save', userView.save, name='save'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)