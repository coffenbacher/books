from books.models import *
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def update_book(request):
    isbn = request.POST.get('ISBN')
    b = Book.objects.get(isbn = isbn)
    price = b.get_current_price()
    return HttpResponse(price)
