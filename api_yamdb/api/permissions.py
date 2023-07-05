from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOnly(BasePermission):
    """
    Доступ у администратора или суперюзера
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает анонимному пользователю безопасные запросы.
    Полный доступ у только у авторизованнорго пользователя с ролью
    администратор.
    """
    message = 'Доступ только у администратора.'

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated and request.user.is_admin))



class AdminModeratorAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )
