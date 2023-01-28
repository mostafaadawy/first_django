from django.db import models
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
