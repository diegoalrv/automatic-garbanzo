from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CatalogoViewSet

router = routers.DefaultRouter()
router.register(r'catalogo',views.CatalogoViewSet, 'catalogo')


# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/catalogo/<str:tematica>/', TuViewSet.as_view({'get': 'retrieve'}), name='tu-recurso-detail'),
    path('a/',views.catalogobytematica)
]