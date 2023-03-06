try:
    from django.conf.urls.defaults import url
except:
    from django.urls import path, include, re_path

from django.conf import settings
from .views import upload, thumbnail_url
from django.urls import path, include, re_path

urlpatterns = [
    re_path(u'^upload/$', upload, name="files_widget_upload"),
    re_path(u'^thumbnail-url/$', thumbnail_url, name="files_widget_get_thumbnail_url"),
]
