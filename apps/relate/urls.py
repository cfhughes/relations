from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.index),
    url(r'^add_shoe', views.add_shoe),
    url(r'^add_person', views.add_person)
]