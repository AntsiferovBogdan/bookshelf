from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

from books.models import Book


def get_books_api(request: HttpRequest) -> JsonResponse:
    books = Book.objects.all().values()
    return JsonResponse(
        list(books),
        safe=False,
        json_dumps_params={'ensure_ascii': False},
        content_type="application/json; charset=utf-8",
        )


def get_book_api(request: HttpRequest, book_id) -> JsonResponse:
    try:
        book = Book.objects.get(id=book_id)
        book_dict = model_to_dict(book)
        return JsonResponse(
            book_dict,
            safe=False,
            json_dumps_params={'ensure_ascii': False},
            content_type="application/json; charset=utf-8",
            )
    except Book.DoesNotExist:
        return JsonResponse({}, status=404)


def get_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by('title')
    return render(
        request,
        'books.html',
        context={
            'books': books,
            }
    )


def get_book_view(request: HttpRequest, book_id) -> HttpResponse:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        book = None
    return render(
        request,
        'book.html',
        context={
            'book': book,
            }
    )
