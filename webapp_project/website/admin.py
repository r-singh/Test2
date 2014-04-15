from __future__ import absolute_import
from django.contrib import admin
from .models import Genre
from .models import Tag
from .models import Book
from .models import Asset


admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Asset)