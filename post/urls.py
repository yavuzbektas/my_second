"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from django.conf.urls import url
from .views import *

app_name='post'

urlpatterns = [

    path('',post_index,name='index'),
    path('index/',post_index,name='index'),
    path('create/',post_create,name='create'),
    path('<slug:slug>/',post_detail,name='detail'),
    path('<slug:slug>/update/',post_update,name='update'),
    path('<slug:slug>/delete/',post_delete,name='delete'),
    # url(r'^index/$', post_index, name="index"),
    #
    # url(r'^create/$', post_create, name='create'),
    #
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #
    # url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
    #
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),


]