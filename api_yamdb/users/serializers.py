from rest_framework import serializers

from reviews.models import User


class UsersSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class NotAdminSerializer(UsersSerializer):
    """
    Сериализатор для модели User.
    Поле 'role' доступно только для чтения.
    """
    role = serializers.CharField(read_only=True)


class SignUpSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации новых пользователей.
    """

    class Meta:
        model = User
        fields = ('email', 'username')


class GetTokenSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения токена.
    """
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
