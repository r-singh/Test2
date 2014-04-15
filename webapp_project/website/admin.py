from __future__ import absolute_import
from django.contrib import admin
from .models import Genre
from .models import Tag
from .models import Book
from .models import Asset
from .models import Author

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ('text', )
    search_fields = ['text']

class AssetAdmin(admin.ModelAdmin):
    list_display = ('book', 'asset_type')
    search_fields = ['book']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']

admin.site.register(Genre, GenreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Author, AuthorAdmin)
