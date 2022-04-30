from django.contrib import admin
from .models import Model, Brand, Generation, Vehicle

admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Generation)
admin.site.register(Vehicle)
