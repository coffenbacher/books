from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render('index.html', request, {})

def update_book(request):
    isbn = request.POST.get('ISBN')
    b = Book.objects.get(isbn = isbn)
    price = b.get_current_price()
    return HttpResponse(price)
