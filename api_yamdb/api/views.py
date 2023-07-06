from rest_framework import viewsets
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Review, Category, Genre, Title
from .serializers import (ReviewSerializer, CategorySerializer,
                          GenreSerializer, TitleSerializer, TitleGETSerializer)
from .permissions import IsAdminOnly, IsAdminOrReadOnly
from .mixins import ModelMixinSet
from .filters import TitleFilter


class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly | IsAdminOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleGETSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'title_id'
