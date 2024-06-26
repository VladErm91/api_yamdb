from rest_framework import serializers

from reviews.models import Review, Category, Genre, Title, Comment


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    Исключает поле 'id'.
    """

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Genre.
    Исключает поле 'id'.
    """

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleGETSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения объектов модели Title.
    Добавляет поле 'rating' для вывода рейтинга.
    """
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')


class TitleSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания/обновления объектов модели Title.
    """
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('name', 'year', 'description', 'genre', 'rating', 'category')

    def to_representation(self, title):
        serializer = TitleGETSerializer(title)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Review.
    Ограничивает поле 'score' диапазоном от 1 до 10.
    """
    author = serializers.ReadOnlyField(source='author.username')
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ['id', 'author', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    """
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
