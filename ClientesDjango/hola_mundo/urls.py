from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('clientes', views.clientes, name="boca"),
    path('contacto', views.contacto, name="contacto"),
    path('actcont', views.actcont, name="actcont"),
    path('infemp', views.infemp, name="infemp"),
] 
