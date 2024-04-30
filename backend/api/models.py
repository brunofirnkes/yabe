from django.db import models

class HasName(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    class Meta:
        abstract = True

class Product(HasName):
    price = models.IntegerField(blank=True, null=True)