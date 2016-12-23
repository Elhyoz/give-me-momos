from django.conf.urls import url
from django.contrib import admin

from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'momos/$', views.momos, name='momos'),
    url(r'momos/new$', views.new_momo, name='new_momo'),
]
