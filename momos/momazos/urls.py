from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'momazos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'momos/$', views.momos, name='momos'),
]
