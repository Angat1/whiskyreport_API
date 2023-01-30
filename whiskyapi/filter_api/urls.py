from django.urls import path, include
from rest_framework import routers
from .views import WhiskyViewSet

router = routers.DefaultRouter()
router.register('whiskies', WhiskyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
