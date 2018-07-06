from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^login', views.home, name = 'home'),
    url(r'^projects', views.login1, name = 'login1'),
    #url(r'^projects/$', views.projects, name = 'projects'),
    url(r'^project/(?P<pk>\d+)/tareas/$', views.index1, name = 'index1'),
    #url(r'^project/(?P<pk>\d+)/tareas/$', views.projects_back, name = 'projects_back'),
    url(r'^horas/(?P<pk>\d+)/$', views.tarea_detail, name = 'tarea_detail'),
    url(r'^horas/(?P<pk>\d+)/$', views.tarea, name = 'tarea'),
    url(r'^logout', views.logout, name = 'logout'),
]
