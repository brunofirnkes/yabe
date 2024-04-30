from rest_framework import serializers
from .models import *

class ProductSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "url")

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price")