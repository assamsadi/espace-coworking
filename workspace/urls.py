"""
URL configuration for workspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/auth/login', permanent=False) ),
    path('admin/', admin.site.urls),
    path('auth/', include('__auth__.urls')),
    path('user/', include('user.urls')),
    path('equipment/', include('equipment.urls')),
    path('salle/', include('salle.urls')),
    path('reservation/', include('reservation.urls')),
    path('staff/', include('staff.urls')),
    path('abonnes/', include('abonnes.urls')),
    path('service/', include('service.urls')),
    path('billet/', include('billet.urls')),
    path('', include('scane.urls')),
    path('sripe/', include('strip.urls')),
    path('Dashboard/', include('dashboard.urls')),
    # path('workspace/', include('__workspace__.urls')),
        path("__reload__/", include("django_browser_reload.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
