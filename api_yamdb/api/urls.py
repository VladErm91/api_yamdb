from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (ReviewViewSet, UsersViewSet, APISignup)


router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
