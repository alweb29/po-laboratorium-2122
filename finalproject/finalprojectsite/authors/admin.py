from django.contrib import admin

# Register your models here.
from .models import Author
from .models import Book
from .models import Award

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Award)