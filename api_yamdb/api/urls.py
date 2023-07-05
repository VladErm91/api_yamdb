from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, UsersViewSet


router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
]
