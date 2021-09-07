from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Comment, CustomUser, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Страница админ. панели произведений."""

    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category'
    )
    search_fields = ('name', 'year', 'category',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Страница админ. панели жанров."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Страница админ. панели категорий."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Страница админ. панели ревью."""

    list_display = ('pk', 'title', 'author', 'text', 'score', 'pub_date')
    search_fields = ('title', 'author', 'text', 'score')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Страница админ. панели комментариев."""

    list_display = ('pk', 'review', 'author', 'text', 'pub_date')
    search_fields = ('author', 'text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'bio', 'role')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'bio', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'role',
                'is_staff',
                'is_active'
            )
        }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
