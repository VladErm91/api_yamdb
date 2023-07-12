from django.contrib import admin
from django.contrib.admin.options import TabularInline

from .models import Category, Genre, GenreTitle, Review, Title, Comment

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
