from django.contrib import admin
from django.contrib.admin.options import TabularInline

from .models import Category, Genre, GenreTitle, Review, Title, Comment
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name',
        'confirmation_code',
    )
    search_fields = ('username', 'role',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


class GenreTitleoInline(TabularInline):
    model = GenreTitle
    min_num = 1
    extra = 1


class TitleAdmin(admin.ModelAdmin):
    inlines = (GenreTitleoInline,)


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Comment)
