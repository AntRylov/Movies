from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Screenshot, Movie, Director, Actor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )


class MovieShotsInLine(admin.TabularInline):
    model = Screenshot
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img scr={obj.image.url} width=>"100" height="110">')

    get_image.short_description = "Image"


class DirectorInLine(admin.TabularInline):
    model = Director
    list_display = ("first_name", "last_name",)
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("first_name", "last_name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110">')

    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category",)
    inlines = [MovieShotsInLine, DirectorInLine, ]
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img scr={obj.poster.url} width=>"100" height="110">')

    get_image.short_description = "Poster"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug": ("first_name", "last_name", )}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110">')

    get_image.short_description = "Image"


admin.site.register(Director)
