from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^particles/$', views.particles, name='particles'),

]
