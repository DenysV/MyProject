from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    #url(r'^', views.home, name = 'home'),
    url(r'^$', views.home, name = 'home'),
    url(r'^accounts/login/$', auth_views.login, name = 'login'),
    url(r'^accounts/projects/$', views.projects_back, name = 'projects_back'),
    url(r'^accounts/project/(?P<pk>\d+)/tareas/$', views.index1, name = 'index1'),
    url(r'^accounts/tarea/(?P<pk>\d+)/horas/$', views.tarea_detail, name = 'tarea_detail'),
    url(r'^accounts/tarea/(?P<pk>\d+)/horas/$', views.tarea, name = 'tarea'),
    url(r'^logout/$', views.logout, name = 'logout'),
    #url(r'^project/(?P<pk>\d+)/tareas/$', views.index1, name = 'index1'),
    #url(r'^project/(?P<pk>\d+)/tareas/$', views.projects_back, name = 'projects_back'),
    #url(r'^horas/(?P<pk>\d+)/$', views.tarea_detail, name = 'tarea_detail'),
    #url(r'^horas/(?P<pk>\d+)/$', views.tarea, name = 'tarea'),
    #url(r'^logout', views.logout, name = 'logout'),
]
