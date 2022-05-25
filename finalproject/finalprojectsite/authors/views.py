
from re import template
from gc import get_objects
from django.template import loader
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Award, Book





def index(request):   
    index_list = 'Author', 'Award', 'Book'
    template = loader.get_template('authors/index.html')
    context = {'index_list': index_list}
    return HttpResponse(template.render(context, request))

def award(request):
    award_list = Award.objects.all
    template = loader.get_template('authors/award.html')
    context = {'award_list':award_list}
    return HttpResponse(template.render(context, request))

def book(request):
    book_list = Book.objects.all
    template = loader.get_template('authors/book.html')
    context = {'book_list':book_list}
    return HttpResponse(template.render(context, request))


def author(request):
    author_list = Author.objects.all
    template = loader.get_template('authors/author.html')
    context = {'author_list':author_list}
    return HttpResponse(template.render(context, request))