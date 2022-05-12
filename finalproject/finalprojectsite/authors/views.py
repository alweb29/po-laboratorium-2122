
from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render





def index(request):
   
    return HttpResponse("authors list")

def award(request):
    response = "You're looking at the awards."
    return HttpResponse(response )

def book(request, ):
    return HttpResponse("You're looking at books.")


def author(request, question_id):
    return HttpResponse("You're looking at authors." )