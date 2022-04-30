from tkinter import CASCADE
from django.db import models
from django.forms import model_to_dict

class Generation(models.Model):
    generation_name = models.CharField(max_length=200)
    def __str__(self):
        return self.generation_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    cars_in_clas = models.ManyToManyField(
        Generation,
        through='Vehicle',
        through_fields=('brand', 'generation', 'model'),
    )
    def __str__(self):
        return self.brand_name

class Model(models.Model):
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name

class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {}'.format(self.brand, self.model, self.generation)