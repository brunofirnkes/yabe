from django.db import models

class HasName(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    class Meta:
        abstract = True

class HasImage(models.Model):
    image_url = models.URLField(default='')
    class Meta:
        abstract = True

class Product(HasName, HasImage):
    price = models.IntegerField(blank=True, null=True)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True)