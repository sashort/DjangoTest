import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import BasicForm 

from . import database
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, "books/book_list.html",context)


def book_detail(request, id):
    book = Book.objects.get(id = id)
    context = {'book_detail': book}
    return render(request, "books/book_detail.html",context)

def hellr(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, "books/book_list.html",context)
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse("<h1>Fianally passed step 1</h1><br><b><u>DESPITE SOMEBODY SITTING ON THE PORCH FOR 10 HRS TODAY TALKING TO MOMMY!</u></b><br><br><h1 style='font-size: 40px;'>Tell Uncle Jim Happy Birthday! 🎂🎂🎂")

class FormBasics(View):
    def get(self, request):
	    form = BasicForm()
		context = {
		    'form': form
	}
	
	return render(request, 'books/forms_basics.html', context)
	def post(self, request):
	    pass