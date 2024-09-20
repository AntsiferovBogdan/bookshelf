from django.contrib import admin
from django.urls import path

from books.views import get_book_api, get_books_api, get_book_view, get_books_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_books_view),
    path('books/<int:book_id>', get_book_view),
    path('api/books/', get_books_api),
    path('api/books/<int:book_id>', get_book_api),
]
