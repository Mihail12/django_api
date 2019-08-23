from rest_framework import filters
from rest_framework.generics import ListAPIView

from api.models import Book, Author
from api.serializers import BookModelSerializer, AuthorModelSerializer


class BookListAPIView(ListAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'published']


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
