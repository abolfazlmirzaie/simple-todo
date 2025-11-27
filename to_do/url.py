from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TaskViewSet

router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')
urlpatterns = router.urls