from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
    UsersViewSet, APISignup, APIGetToken, CommentViewSet
)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='сategories')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register('users', UsersViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
