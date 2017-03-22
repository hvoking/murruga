from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^maps/$', views.maps, name='mapa'),
    url(r'^mapa2/$', views.mapa2, name='mapa2'),
    
]
