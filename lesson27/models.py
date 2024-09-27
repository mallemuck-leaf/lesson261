from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=11, decimal_places=2)

    def absolute_url(self):
        return reverse('name-detail', args=[str(self.name)])

    def __str__(self):
        return self.name
