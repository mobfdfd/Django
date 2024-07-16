from rest_framework import serializers
from .models import ShoppingCart

class ShoppingCartSerializer(serializers.ModelSerializer):
    product_brand = serializers.ReadOnlyField(source='product.brand')
    product_article = serializers.ReadOnlyField(source='product.article')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = ShoppingCart
        fields = ['id', 'product_brand', 'product_article', 'product_price']
