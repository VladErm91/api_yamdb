from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reviews.models import Title, Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        title_id = kwargs.get('title_id')
        try:
            title = Title.objects.get(pk=title_id)
        except Title.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if Review.objects.filter(title=title, author=request.user).exists():
            return Response({'detail': 'Review already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, title=title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
