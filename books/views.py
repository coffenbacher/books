from books.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})
