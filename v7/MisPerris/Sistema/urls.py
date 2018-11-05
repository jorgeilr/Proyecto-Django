from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^gestionUsuario/$',views.gestionarUsuarios,name="gestionUsuario"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),

    ]