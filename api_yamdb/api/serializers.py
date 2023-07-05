from rest_framework import serializers

from reviews.models import Review, User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class NotAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        read_only_fields = ('role',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = ['id', 'review_text', 'author', 'score', 'pub_date']
        read_only_fields = ['id', 'author', 'pub_date']


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'username'
        )
