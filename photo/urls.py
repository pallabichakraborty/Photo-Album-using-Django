# Code Reference: https://github.com/buckyroberts/Viberr

from django.conf.urls import url
from . import views

app_name = "photo"

urlpatterns = [
    # Homepage for the photos
    # /photo/
    url(r'^$', views.index, name='index'),
    # Detail View of a particular photo
    # /photo/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # Add a Photo
    # /photo/photo/add/
    url(r'photo/add/$', views.photoupload, name='photo-add'),

    # /photo/photo/2/
    url(r'photo/update/(?P<pk>[0-9]+)/$', views.PhotoUpdate.as_view(), name='photo-update'),
    # /photo/photo/2/delete/
    url(r'photo/(?P<pk>[0-9]+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),
    # See the photos uploaded by the user
    url(r'photo/myuploads/$', views.userphotoview, name='myuploads'),
    # Register user
    url(r'^register/$', views.register, name='register'),
    # Login user
    url(r'^login/$', views.login_user, name='login'),
    # Logout user
    url(r'^logout/$', views.logout_user, name='logout'),
]
