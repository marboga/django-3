print "gold app"
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^house', views.house, name='house'),
    url(r'^cave', views.cave, name='cave'),
    url(r'^casino', views.casino, name='casino'),
    url(r'^farm', views.farm, name='farm'),
]
