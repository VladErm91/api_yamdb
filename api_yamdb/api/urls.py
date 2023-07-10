from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
    UsersViewSet, APISignup, APIGetToken, CommentViewSet
)

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='сategories')
router_v1.register('genres', GenreViewSet, basename='genre')
router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register('users', UsersViewSet, basename='users')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
