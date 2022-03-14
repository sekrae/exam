from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    first_number = models.IntegerField(null=True)
    balance_group = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.Model)
    unique_number = models.IntegerField(unique=True)
    initial_cost = models.IntegerField(null=True)
    residual_value = models.IntegerField(null=True)

    def __str__(self):
        return self.name

