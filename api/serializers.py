from rest_framework import serializers

from api.models import Book, Author


class BookForAuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id']


class AuthorModelSerializer(serializers.ModelSerializer):
    books = BookForAuthorModelSerializer(many=True)

    class Meta:
        model = Author
        exclude = ['id']


class AuthorForBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['id']


class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorForBookModelSerializer()

    class Meta:
        model = Book
        exclude = ['id']



