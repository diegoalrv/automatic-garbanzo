from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CatalogoViewSet

router = routers.DefaultRouter()
router.register(r'api/catalogo',views.CatalogoViewSet, 'catalogo')


urlpatterns = router.urls