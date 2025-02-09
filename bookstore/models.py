import django
from django.db import models
from django.db.models.functions import Now
from datetime import datetime

from .base_models import BaseModel

class Author(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    birth_date = models.DateField(db_default=Now(), default=datetime.now(), db_index=True)

class Book(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_index=True)
    published_date = models.DateField(db_default=Now(), default=datetime.now(), db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Publisher(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    books = models.ManyToManyField(Book)
    
class Store(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    books = models.ManyToManyField(Book)
    publishers = models.ManyToManyField(Publisher)