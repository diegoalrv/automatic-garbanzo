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
    path('api/<str:column>/<str:value>',views.catalogoByColumn),
    # path('api/catalogo/tematica/<str:value>',views.PruebaSetTematica.as_view({'get':'list'}))
    # path('api/catalogo/tematica/<str:value>',views.PruebaSetTematica.as_view()),
    path('tematica/<str:value>/', views.TestModelView.as_view({'get': 'list'}), name='mi-modelo-list'),



]