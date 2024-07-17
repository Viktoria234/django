from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def html_response(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})