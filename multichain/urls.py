

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^info', views.info, name='info'),
    url(r'^index', views.index, name='index'),
    url(r'^homepage', views.user_homepage, name='homepage'),

]