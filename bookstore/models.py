import django
from django.db import models
from django.db.models.functions import Now
import django.utils.timezone

from .base_models import BaseModel

class Author(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    birth_date = models.DateField(db_default=Now(), default=django.utils.timezone.now, db_index=True)

    def __str__(self):
        return self.name

class Book(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_index=True)
    published_date = models.DateField(db_default=Now(), default=django.utils.timezone.now, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class Publisher(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name

class Store(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    books = models.ManyToManyField(Book)
    publishers = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name