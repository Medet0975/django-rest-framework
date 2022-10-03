from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Products(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='post_image', max_length=255)
    # book = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    cat_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.cat_id} -> {self.name}'

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f'{self.name}'





