from django.urls import path
from . import views

urlpatterns = [
    path('', views.pruebatempl),
    path('ruta/<str:algo>', views.prueba)

]