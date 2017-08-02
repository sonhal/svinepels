

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^info', views.info, name='info'),
    url(r'^index', views.index, name='index'),
    url(r'^homepage', views.user_homepage, name='homepage'),
    url(r'^makkeaddress', views.make_address, name='makeaddress'),
    #url(r'^register', views.register, name='register'),

]