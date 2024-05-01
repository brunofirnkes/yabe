from rest_framework import serializers
from .models import *

class ProductSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "url", "image_url", "price")

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "url", "image_url", "price")