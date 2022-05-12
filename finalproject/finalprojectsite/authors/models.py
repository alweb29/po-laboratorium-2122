from operator import mod
from django.db import models

# Create your models here.
class Award (models.Model):
    awardName_text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.awardName_text

class Book (models.Model):   
    bookTitle_text = models.CharField(max_length=200)
    Award = models.ForeignKey(Award, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookTitle_text

class Author(models.Model):
    authorName_text = models.CharField(max_length=200)
    books = models.ManyToManyField(
        Book  
    )

    def __str__(self):
        return self.authorName_text