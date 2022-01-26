from rest_framework.routers import DefaultRouter

from .viewsets import TestViewSet

router = DefaultRouter()
router.register('test', TestViewSet, basename='test')

urlpatterns = router.urls
