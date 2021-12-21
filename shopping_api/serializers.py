from rest_framework import serializers
from .models import Product, Category, Basket


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
