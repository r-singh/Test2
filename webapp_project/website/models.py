from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Tag(models.Model):
    text = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn_10 = models.CharField(max_length=30,blank=True, null=True)
    isbn_13 = models.CharField(max_length=30, blank=True, null=True)
    amazon_url =  models.CharField(max_length=30, blank=True, null=True,)
    genres =  models.ManyToManyField(Genre, related_name="books", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="books", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="books", blank=True, null=True)


class Asset(models.Model):
    ASSET_TYPES = (
        ("epub", "EPUB"),
        ("pdf", "PDF"),
        ("mobi", "MOBI"),
        ("other", "OTHER")
    )
    book = models.ForeignKey(Book, related_name="assets")
    path =  models.CharField(max_length=400)
    original_file_path =  models.CharField(max_length=400)
    asset_type = models.CharField(choices=ASSET_TYPES, max_length=5)