# Code Reference: https://github.com/buckyroberts/Viberr

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^photo/',include('photo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView,name='home')
]

# Links for setting the folder to save the media files
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)