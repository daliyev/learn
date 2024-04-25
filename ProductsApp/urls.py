from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, AppViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('apps', AppViewSet)

urlpatterns = [
    path('', include(router.urls)),
]