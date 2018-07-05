from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^login', views.login1, name = 'login1'),
    #url(r'^projects/$', views.projects, name = 'projects'),
    url(r'^project/(?P<pk>\d+)/tareas/$', views.index1, name = 'index1'),
    url(r'^horas/(?P<pk>\d+)/$', views.tarea_detail, name = 'tarea_detail'),
    url(r'^horas/(?P<pk>\d+)/$', views.tarea, name = 'tarea'),
    url(r'^logout', views.logout, name = 'logout'),
]
