from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    #url(r'^project/(?P<pk>\d+)/$', views.project_detail, name = 'project_detail'),
    url(r'^index/$', views.index, name = 'index'),
    #url(r'^accounts/invalid/$', views.login, name = 'invalid'),
]
