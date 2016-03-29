from django.conf.urls import include, url
from gold import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_money', views.process_money, name='process_money'),
]
