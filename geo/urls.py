from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^maps/$', views.maps, name='mapa'),
    url(r'^mapa2/$', views.mapa2, name='mapa2'),
    url(r'^mapa3/$', views.mapa2, name='mapa3'),
    url(r'^mapa3d/$', views.mapa3d, name='mapa3d'),
]
