from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('book/', views.book, name='book'),
    # ex: /polls/5/results/
    path('award/', views.award, name='award'),
    # ex: /polls/5/vote/
    path('author/', views.author, name='author'),
]