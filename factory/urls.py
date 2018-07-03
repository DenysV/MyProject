from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^login', views.login1, name = 'login1'),
    url(r'^index/(?P<pk>\d+)/$', views.index, name = 'index'),
    url(r'^project/(?P<pk>\d+)/$', views.tarea, name = 'tarea'),
    url(r'^horas/$', views.tarea_detail, name = 'tarea_detail'),
]
