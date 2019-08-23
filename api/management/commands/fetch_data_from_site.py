import datetime

import requests
from django.core.management import BaseCommand

from api.models import Book, Author


class Command(BaseCommand):
    help = "fetch data to project from https://hokodo-frontend-interview.netlify.com/data.json"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to fetch data'))
        response = requests.get('https://hokodo-frontend-interview.netlify.com/data.json', timeout=15)
        if response.status_code == 200:
            response = response.json()
            if response.get('books', None):
                for book in response['books']:
                    author, _ = Author.objects.get_or_create(
                        name=book['author']
                    )
                    published = datetime.datetime.strptime(book['published'], "%Y-%m-%dT%H:%M:%S.%f%z") if book.get('published', None) else None
                    Book.objects.get_or_create(
                        external_id=book['id'],
                        cover=book.get('cover', None),
                        isbn=book.get('isbn', None),
                        title=book.get('title', None),
                        published=published,
                        publisher=book.get('publisher', None),
                        pages=book.get('pages', None),
                        description=book.get('description', None),
                        website=book.get('website', None),
                        author=author
                    )
            else:
                self.stdout.write(self.style.Error('Site data has been changed'))
        else:
            self.stdout.write(self.style.Error('Site is not reachable'))


