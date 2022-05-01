from django.db import models

# Create your models here.
class Author(models.Model):
    authorName_text = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date published')

    def __str__(self):
        return self.authorName_text

class Book (models.Model):
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    bookTitle_text = models.CharField(max_length=200)
    bookRate = models.IntegerField(default=0)
    
    def __str__(self):
        return self.bookTitle_text

class Award (models.Model):
    awardName_text = models.CharField(max_length=100)
    awardedAuthors = models.ManyToManyField(Author)

    def __str__(self):
        return self.awardName_text
