from django.db import models
from django.db.models.functions import Now
from datetime import datetime


class BaseModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now(),verbose_name='Creation Time')
    updated_at = models.DateTimeField(verbose_name='Update Time', null=True, blank=True)
    is_deleted = models.BooleanField(default=False, db_default=Now(),verbose_name='Deletion Flag')

    class Meta:
        # Abstract model, not created in the database
        abstract = True