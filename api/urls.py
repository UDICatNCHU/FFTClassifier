from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from api import views

urlpatterns = [
  url(r'^bayes/$', views.bayes),
]