import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView, Book

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())

def book_list(request):
	books = Book.objects.all()
	context = {'book_list':books}
	print(context)
	return render(request, "books/book_list.html",context)


def book_detail(request, id):
	book = Book.objects.get(id = id)
	context = {'book_detail': book}
	return render(request, "books/book_detail.html",context)

def hellr(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse("<h1>Fianally passed step 1</h1><br><b><u>DESPITE SOMEBODY SITTING ON THE PORCH FOR 10 HRS TODAY TALKING TO MOMMY!</u></b><br><br><h1 style='font-size: 40px;'>Tell Uncle Jim Happy Birthday! 🎂🎂🎂")
