from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('books/', views.book, name='book'),
    # ex: /polls/5/results/
    path('awards/', views.award, name='award'),
    # ex: /polls/5/vote/
    path('authors/', views.author, name='author'),
]