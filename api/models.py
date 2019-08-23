from django.db import models


class BaseCreatedModifiedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # PyCharm doesn't autocomplete without it :-(

    class Meta:
        abstract = True


# Create your models here.
class Book(BaseCreatedModifiedModel):
    external_id = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    cover = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    isbn = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    author = models.ForeignKey('Author', null=True, related_name='books', on_delete=models.SET_NULL)
    published = models.DateTimeField(null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    pages = models.IntegerField(null=True)
    description = models.TextField(null=True)
    website = models.CharField(max_length=255, blank=True, null=True, db_index=True)


class Author(BaseCreatedModifiedModel):
    name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
