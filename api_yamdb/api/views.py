from django.db.models import Avg
from django.shortcuts import get_object_or_404

from rest_framework import filters, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Review, Category, Genre, Title

from .filters import TitleFilter
from .mixins import ModelMixinSet
from .permissions import (
    IsAdminOrReadOnly,
    AdminModeratorAuthorPermission
)
from .serializers import (
    ReviewSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitleGETSerializer,
    CommentSerializer
)


class CategoryViewSet(ModelMixinSet):
    """
    Представление для просмотра и изменения экземпляров категории.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    lookup_field = 'slug'


class GenreViewSet(ModelMixinSet):
    """
    Представление для просмотра и изменения экземпляров жанра.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """
    Представление для просмотра и изменения экземпляров тайтла.
    """
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleGETSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Представление для просмотра и изменения экземпляров отзывов.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminModeratorAuthorPermission,)

    def create(self, request, *args, **kwargs):
        title_id = kwargs.get('title_id')
        try:
            title = Title.objects.get(pk=title_id)
        except Title.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if Review.objects.filter(title=title, author=request.user).exists():
            return Response({'detail': 'Review already exists'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, title=title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Представление для просмотра и изменения экземпляров комментариев.
    """
    serializer_class = CommentSerializer
    permission_classes = (AdminModeratorAuthorPermission,)

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
