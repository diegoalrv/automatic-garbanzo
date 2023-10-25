from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CatalogoViewSet

router = routers.DefaultRouter()
# router.register(r'catalogo',views.CatalogoViewSet, 'catalogo') # era el antiguo clase de catalogo


# urlpatterns = router.urls

urlpatterns = [
    path('', views.home),
    path('api/', include(router.urls)),
    path('api/<str:column>/<str:value>',views.CatalogoViewSet.as_view({'get': 'list'})),


]